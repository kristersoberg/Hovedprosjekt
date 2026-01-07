#!/usr/bin/env python3
"""
Metrics Dashboard for Cisco Configuration Documentation System

Displays processing metrics and statistics from the SQLite database.
"""

import sys
from pathlib import Path
from datetime import datetime
from metrics_tracker import MetricsTracker


class MetricsDashboard:
    """Display metrics and statistics."""

    def __init__(self, db_path: Path):
        """
        Initialize dashboard.

        Args:
            db_path: Path to metrics database
        """
        self.tracker = MetricsTracker(db_path)

    def display_summary(self):
        """Display summary statistics."""
        stats = self.tracker.get_summary_stats()

        if not stats or stats.get('total_configs', 0) == 0:
            print("\n No metrics data available yet.")
            print("   Process some configurations to see statistics.\n")
            return

        print("\n" + "=" * 70)
        print("   METRICS DASHBOARD - SUMMARY STATISTICS")
        print("=" * 70)
        print()

        # Overall stats
        print(" Overall Statistics:")
        print(f"   Total Configurations Processed: {stats['total_configs']}")
        print(f"   Successful: {stats['total_configs'] - stats['error_count']}")
        print(f"   Failed: {stats['error_count']}")

        if stats['total_configs'] > 0:
            success_rate = ((stats['total_configs'] - stats['error_count']) / stats['total_configs']) * 100
            print(f"   Success Rate: {success_rate:.1f}%")
        print()

        # Performance stats
        print("  Performance Metrics:")
        print(f"   Average Total Time: {stats['avg_total_time_seconds']:.2f}s")
        print(f"   Average Parse Time: {stats['avg_parse_time_seconds']:.2f}s")
        print(f"   Average LLM Time: {stats['avg_llm_time_seconds']:.2f}s")
        print()

        # Accuracy stats
        if stats['avg_accuracy_percent'] > 0:
            print(" Validation Metrics:")
            print(f"   Average Accuracy: {stats['avg_accuracy_percent']:.1f}%")
            print()

        # Token usage
        if stats['avg_tokens'] > 0:
            print(" Token Usage:")
            print(f"   Average Tokens per Config: {stats['avg_tokens']}")
            print()

    def display_recent(self, limit: int = 10):
        """
        Display recent processing runs.

        Args:
            limit: Number of recent runs to show
        """
        recent = self.tracker.get_recent_metrics(limit)

        if not recent:
            print("\n No recent processing runs found.\n")
            return

        print("=" * 70)
        print(f"   RECENT PROCESSING RUNS (Last {len(recent)})")
        print("=" * 70)
        print()

        for i, run in enumerate(recent, 1):
            status = " FAILED" if run['error_occurred'] else " Success"

            print(f"{i}. {run['config_file']}")
            print(f"   Status: {status}")
            print(f"   Time: {run['timestamp']}")

            if not run['error_occurred']:
                print(f"   Processing Time: {run['total_time_seconds']:.2f}s")
                if run['validation_accuracy_percent']:
                    print(f"   Accuracy: {run['validation_accuracy_percent']:.1f}%")
                if run['total_tokens']:
                    print(f"   Tokens: {run['total_tokens']}")

            print()

    def display_detailed_stats(self):
        """Display detailed statistics by querying the database."""
        cursor = self.tracker.conn.execute('''
            SELECT
                COUNT(*) as total,
                MIN(total_time_seconds) as min_time,
                MAX(total_time_seconds) as max_time,
                MIN(validation_accuracy_percent) as min_accuracy,
                MAX(validation_accuracy_percent) as max_accuracy,
                SUM(total_tokens) as total_tokens_used
            FROM processing_metrics
            WHERE error_occurred = 0
        ''')

        row = cursor.fetchone()

        if row and row[0] > 0:
            print("=" * 70)
            print("   DETAILED STATISTICS")
            print("=" * 70)
            print()

            print("⏱  Processing Time Range:")
            print(f"   Fastest: {row[1]:.2f}s")
            print(f"   Slowest: {row[2]:.2f}s")
            print()

            if row[3] is not None:
                print(" Accuracy Range:")
                print(f"   Lowest: {row[3]:.1f}%")
                print(f"   Highest: {row[4]:.1f}%")
                print()

            if row[5]:
                print(" Total Tokens Used:")
                print(f"   {row[5]:,} tokens across all processing runs")
                print()

    def export_to_csv(self, output_path: Path):
        """
        Export metrics to CSV file.

        Args:
            output_path: Path to save CSV file
        """
        self.tracker.export_to_csv(output_path)
        print(f"\n Metrics exported to: {output_path}\n")

    def display_full_dashboard(self):
        """Display complete dashboard."""
        self.display_summary()
        self.display_detailed_stats()
        self.display_recent(limit=5)

        print("=" * 70)
        print()
        print(" Tips:")
        print("   • Export to CSV: python metrics_dashboard.py --export metrics.csv")
        print("   • View more recent runs: python metrics_dashboard.py --recent 20")
        print()


def main():
    """Main entry point."""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    metrics_db = project_root / "metrics" / "processing_metrics.db"

    if not metrics_db.exists():
        print("\n Error: Metrics database not found.")
        print(f"   Expected location: {metrics_db}")
        print("   Process some configurations first to generate metrics.\n")
        sys.exit(1)

    dashboard = MetricsDashboard(metrics_db)

    # Parse command line arguments
    if "--export" in sys.argv:
        try:
            export_index = sys.argv.index("--export")
            if export_index + 1 < len(sys.argv):
                output_file = Path(sys.argv[export_index + 1])
                dashboard.export_to_csv(output_file)
            else:
                print(" Error: --export requires a filename")
                sys.exit(1)
        except Exception as e:
            print(f" Error exporting: {e}")
            sys.exit(1)

    elif "--recent" in sys.argv:
        try:
            recent_index = sys.argv.index("--recent")
            if recent_index + 1 < len(sys.argv):
                limit = int(sys.argv[recent_index + 1])
                dashboard.display_recent(limit)
            else:
                dashboard.display_recent()
        except ValueError:
            print(" Error: --recent requires a number")
            sys.exit(1)

    elif "--summary" in sys.argv:
        dashboard.display_summary()

    elif "--detailed" in sys.argv:
        dashboard.display_detailed_stats()

    else:
        # Show full dashboard by default
        dashboard.display_full_dashboard()


if __name__ == "__main__":
    main()
