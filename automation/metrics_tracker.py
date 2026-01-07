#!/usr/bin/env python3
"""
Metrics Tracker for Cisco Configuration Documentation System

Tracks processing metrics in a SQLite database for research analysis.
"""

import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List


class MetricsTracker:
    """Track and store processing metrics in SQLite database."""

    def __init__(self, db_path: Path):
        """
        Initialize metrics tracker.

        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self._create_tables()

    def _create_tables(self):
        """Create database tables if they don't exist."""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS processing_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                config_file TEXT NOT NULL,
                timestamp DATETIME NOT NULL,
                parse_time_seconds REAL,
                llm_call_time_seconds REAL,
                total_time_seconds REAL,
                validation_accuracy_percent REAL,
                total_validation_checks INTEGER,
                failed_validation_checks INTEGER,
                config_size_bytes INTEGER,
                generated_doc_size_bytes INTEGER,
                llm_model TEXT,
                llm_temperature REAL,
                prompt_tokens INTEGER,
                completion_tokens INTEGER,
                total_tokens INTEGER,
                secrets_sanitized INTEGER,
                validation_enabled BOOLEAN,
                error_occurred BOOLEAN,
                error_message TEXT
            )
        ''')
        self.conn.commit()

    def record_processing(self, metrics: Dict[str, Any]):
        """
        Record processing metrics for a configuration file.

        Args:
            metrics: Dictionary containing metric values
        """
        self.conn.execute('''
            INSERT INTO processing_metrics (
                config_file,
                timestamp,
                parse_time_seconds,
                llm_call_time_seconds,
                total_time_seconds,
                validation_accuracy_percent,
                total_validation_checks,
                failed_validation_checks,
                config_size_bytes,
                generated_doc_size_bytes,
                llm_model,
                llm_temperature,
                prompt_tokens,
                completion_tokens,
                total_tokens,
                secrets_sanitized,
                validation_enabled,
                error_occurred,
                error_message
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            metrics.get('config_file'),
            metrics.get('timestamp', datetime.now()),
            metrics.get('parse_time_seconds'),
            metrics.get('llm_call_time_seconds'),
            metrics.get('total_time_seconds'),
            metrics.get('validation_accuracy_percent'),
            metrics.get('total_validation_checks'),
            metrics.get('failed_validation_checks'),
            metrics.get('config_size_bytes'),
            metrics.get('generated_doc_size_bytes'),
            metrics.get('llm_model'),
            metrics.get('llm_temperature'),
            metrics.get('prompt_tokens'),
            metrics.get('completion_tokens'),
            metrics.get('total_tokens'),
            metrics.get('secrets_sanitized', 0),
            metrics.get('validation_enabled', True),
            metrics.get('error_occurred', False),
            metrics.get('error_message'),
        ))
        self.conn.commit()

    def get_summary_stats(self) -> Dict[str, Any]:
        """
        Get summary statistics across all processed configurations.

        Returns:
            Dictionary with summary statistics
        """
        cursor = self.conn.execute('''
            SELECT
                COUNT(*) as total_configs,
                AVG(total_time_seconds) as avg_total_time,
                AVG(parse_time_seconds) as avg_parse_time,
                AVG(llm_call_time_seconds) as avg_llm_time,
                AVG(validation_accuracy_percent) as avg_accuracy,
                AVG(total_tokens) as avg_tokens,
                SUM(CASE WHEN error_occurred = 1 THEN 1 ELSE 0 END) as error_count
            FROM processing_metrics
        ''')

        row = cursor.fetchone()
        if row:
            return {
                'total_configs': row[0],
                'avg_total_time_seconds': round(row[1], 2) if row[1] else 0,
                'avg_parse_time_seconds': round(row[2], 2) if row[2] else 0,
                'avg_llm_time_seconds': round(row[3], 2) if row[3] else 0,
                'avg_accuracy_percent': round(row[4], 2) if row[4] else 0,
                'avg_tokens': int(row[5]) if row[5] else 0,
                'error_count': row[6] or 0,
            }
        return {}

    def get_recent_metrics(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent processing metrics.

        Args:
            limit: Number of recent records to retrieve

        Returns:
            List of metric dictionaries
        """
        cursor = self.conn.execute('''
            SELECT
                config_file,
                timestamp,
                total_time_seconds,
                validation_accuracy_percent,
                total_tokens,
                error_occurred
            FROM processing_metrics
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))

        results = []
        for row in cursor.fetchall():
            results.append({
                'config_file': row[0],
                'timestamp': row[1],
                'total_time_seconds': row[2],
                'validation_accuracy_percent': row[3],
                'total_tokens': row[4],
                'error_occurred': bool(row[5]),
            })

        return results

    def export_to_csv(self, output_path: Path):
        """
        Export all metrics to CSV file for analysis.

        Args:
            output_path: Path to save CSV file
        """
        import csv

        cursor = self.conn.execute('SELECT * FROM processing_metrics')
        columns = [description[0] for description in cursor.description]

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(cursor.fetchall())

    def close(self):
        """Close database connection."""
        self.conn.close()


# Global metrics tracker instance
_tracker: Optional[MetricsTracker] = None


def init_metrics(db_path: Path) -> MetricsTracker:
    """
    Initialize global metrics tracker.

    Args:
        db_path: Path to SQLite database file

    Returns:
        MetricsTracker instance
    """
    global _tracker
    _tracker = MetricsTracker(db_path)
    return _tracker


def get_metrics() -> Optional[MetricsTracker]:
    """
    Get global metrics tracker instance.

    Returns:
        MetricsTracker instance or None if not initialized
    """
    return _tracker
