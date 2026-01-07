#!/usr/bin/env python3
"""
Logging System for Cisco Configuration Documentation

Provides structured logging with configurable verbosity levels.
Logs are written to both console and log files.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional


class DocumentationLogger:
    """Centralized logging for the documentation system."""

    def __init__(self, log_dir: Path, verbose: bool = False, debug: bool = False):
        """
        Initialize logging system.

        Args:
            log_dir: Directory to store log files
            verbose: Enable verbose output (INFO level)
            debug: Enable debug output (DEBUG level)
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        # Determine log level
        if debug:
            self.log_level = logging.DEBUG
            self.console_level = logging.DEBUG
        elif verbose:
            self.log_level = logging.DEBUG  # File always gets debug
            self.console_level = logging.INFO
        else:
            self.log_level = logging.DEBUG  # File always gets debug
            self.console_level = logging.WARNING

        # Create logger
        self.logger = logging.getLogger("cisco_doc_generator")
        self.logger.setLevel(self.log_level)
        self.logger.handlers.clear()  # Clear any existing handlers

        # Create formatters
        detailed_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        console_formatter = logging.Formatter(
            '%(levelname)-8s | %(message)s'
        )

        # File handler - always detailed logging
        log_file = self.log_dir / f"documentation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        self.logger.addHandler(file_handler)

        # Console handler - configurable verbosity with UTF-8 encoding
        import io
        console_handler = logging.StreamHandler(io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace'))
        console_handler.setLevel(self.console_level)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        self.log_file_path = log_file

    def debug(self, message: str, exc_info: bool = False):
        """Log debug message."""
        self.logger.debug(message, exc_info=exc_info)

    def info(self, message: str, exc_info: bool = False):
        """Log info message."""
        self.logger.info(message, exc_info=exc_info)

    def warning(self, message: str, exc_info: bool = False):
        """Log warning message."""
        self.logger.warning(message, exc_info=exc_info)

    def error(self, message: str, exc_info: bool = False):
        """Log error message."""
        self.logger.error(message, exc_info=exc_info)

    def critical(self, message: str, exc_info: bool = False):
        """Log critical message."""
        self.logger.critical(message, exc_info=exc_info)

    def section(self, title: str):
        """Log a section header (always visible)."""
        separator = "=" * 60
        self.logger.info(f"\n{separator}")
        self.logger.info(f" {title}")
        self.logger.info(separator)

    def step(self, step_name: str):
        """Log a processing step (visible in normal mode)."""
        self.logger.warning(f"▶ {step_name}")

    def success(self, message: str):
        """Log success message (always visible)."""
        self.logger.warning(f"✓ {message}")

    def progress(self, message: str):
        """Log progress message (visible only in verbose mode)."""
        self.logger.info(f"  {message}")

    def get_log_path(self) -> Path:
        """Get the path to the current log file."""
        return self.log_file_path


# Global logger instance
_logger: Optional[DocumentationLogger] = None


def init_logger(log_dir: Path, verbose: bool = False, debug: bool = False) -> DocumentationLogger:
    """
    Initialize the global logger instance.

    Args:
        log_dir: Directory to store log files
        verbose: Enable verbose output
        debug: Enable debug output

    Returns:
        DocumentationLogger instance
    """
    global _logger
    _logger = DocumentationLogger(log_dir, verbose, debug)
    return _logger


def get_logger() -> DocumentationLogger:
    """
    Get the global logger instance.

    Returns:
        DocumentationLogger instance

    Raises:
        RuntimeError: If logger hasn't been initialized
    """
    global _logger
    if _logger is None:
        raise RuntimeError("Logger not initialized. Call init_logger() first.")
    return _logger
