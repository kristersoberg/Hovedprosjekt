#!/usr/bin/env python3
"""
File Watcher for Cisco Configuration Files

Monitors the configs/ directory for new or modified .txt files and
automatically triggers the processor for each change.
"""

import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ConfigFileHandler(FileSystemEventHandler):
    """Handler for configuration file changes."""

    def __init__(self, configs_dir: Path, processor_script: Path):
        self.configs_dir = configs_dir
        self.processor_script = processor_script
        self.processing_lock = set()
        self.cooldown = {}  # File path -> last processing time

    def on_created(self, event):
        """Handle file creation."""
        if not event.is_directory and event.src_path.endswith('.txt'):
            print(f"\n📄 New file detected: {Path(event.src_path).name}")
            self._process_file(event.src_path)

    def on_modified(self, event):
        """Handle file modification."""
        if not event.is_directory and event.src_path.endswith('.txt'):
            # Check cooldown to avoid duplicate processing
            current_time = time.time()
            last_time = self.cooldown.get(event.src_path, 0)

            if current_time - last_time > 2:  # 2 second cooldown
                print(f"\n📝 File changed: {Path(event.src_path).name}")
                self._process_file(event.src_path)
                self.cooldown[event.src_path] = current_time

    def _process_file(self, file_path: str):
        """Process a configuration file."""
        file_path = Path(file_path)

        # Prevent duplicate processing
        if file_path in self.processing_lock:
            print(f"⏭️  Skipping {file_path.name} (already processing)")
            return

        self.processing_lock.add(file_path)
        print(f"⚙️  Processing: {file_path.name}")
        print(f"   Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        try:
            # Run processor
            result = subprocess.run(
                [sys.executable, str(self.processor_script), str(file_path)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(f"✅ Completed: {file_path.name}")
            else:
                print(f"❌ Failed: {file_path.name} (exit code: {result.returncode})")
                if result.stderr:
                    print(f"   Error: {result.stderr}")

        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {str(e)}")

        finally:
            self.processing_lock.discard(file_path)
            print("───────────────────────────────────────")


def main():
    """Main entry point."""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    configs_dir = project_root / "configs"
    processor_script = script_dir / "processor.py"

    # Ensure configs directory exists
    configs_dir.mkdir(exist_ok=True)

    print("🔍 Starting Cisco Config Watcher...")
    print(f"📁 Monitoring directory: {configs_dir}")
    print("───────────────────────────────────────")

    # Create event handler and observer
    event_handler = ConfigFileHandler(configs_dir, processor_script)
    observer = Observer()
    observer.schedule(event_handler, str(configs_dir), recursive=False)

    # Start observer
    observer.start()
    print("\n✅ Watcher ready and monitoring for changes")
    print("   Press Ctrl+C to stop\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down watcher...")
        observer.stop()
        observer.join()
        print("✅ Watcher stopped")


if __name__ == "__main__":
    main()