#!/usr/bin/env python3
"""
Test Runner for Cisco Documentation System

Runs all test suites and generates a summary report.
"""

import sys
import unittest
from pathlib import Path


def run_all_tests():
    """Run all test suites."""
    # Discover and run tests
    loader = unittest.TestLoader()
    test_dir = Path(__file__).parent
    suite = loader.discover(str(test_dir), pattern='test_*.py')

    # Run with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    print("  TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    if result.wasSuccessful():
        print("\nAll tests passed!")
        return 0
    else:
        print("\nSome tests failed.")
        return 1


def run_specific_suite(suite_name):
    """
    Run a specific test suite.

    Args:
        suite_name: Name of test file (e.g., 'test_config_parser')
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(suite_name)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Run specific suite
        suite_name = sys.argv[1]
        sys.exit(run_specific_suite(suite_name))
    else:
        # Run all tests
        sys.exit(run_all_tests())
