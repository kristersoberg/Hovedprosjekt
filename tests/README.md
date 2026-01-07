# Automated Test Suite

Comprehensive automated tests for the Cisco Configuration Documentation System.

## Test Structure

```
tests/
├── test_config_parser.py    # Unit tests for config parsing
├── test_validator.py         # Unit tests for documentation validation
├── test_integration.py       # End-to-end integration tests
├── run_tests.py             # Test runner script
└── fixtures/                # Test data
    ├── sample_configs/      # Sample Cisco configurations
    └── expected_outputs/    # Expected output files
```

## Running Tests

### Run All Tests

```bash
# From project root
python tests/run_tests.py

# Or using unittest directly
python -m unittest discover tests -v
```

### Run Specific Test Suite

```bash
# Config parser tests only
python -m unittest tests.test_config_parser -v

# Validator tests only
python -m unittest tests.test_validator -v

# Integration tests only
python -m unittest tests.test_integration -v
```

### Run Specific Test

```bash
# Run a specific test class
python -m unittest tests.test_config_parser.TestCiscoConfigParser -v

# Run a specific test method
python -m unittest tests.test_config_parser.TestCiscoConfigParser.test_extract_vlans -v
```

## Test Coverage

### Config Parser Tests (`test_config_parser.py`)
- ✓ Configuration file loading
- ✓ Device information extraction (hostname, IOS version)
- ✓ VLAN extraction (IDs and names)
- ✓ Interface extraction (physical, descriptions, modes)
- ✓ Routing extraction (static routes, protocols)
- ✓ Management configuration extraction
- ✓ Secrets sanitization
- ✓ Edge cases (invalid files, empty configs)

### Validator Tests (`test_validator.py`)
- ✓ Hostname validation
- ✓ IOS version validation
- ✓ VLAN presence validation
- ✓ IP address validation
- ✓ Accuracy calculation
- ✓ Validation report structure
- ✓ Edge cases (empty documentation, missing data)

### Integration Tests (`test_integration.py`)
- ✓ End-to-end parsing workflow
- ✓ Prompt building from structured data
- ✓ Validation of generated documentation
- ✓ Secrets sanitization in full workflow
- ✓ Error handling (invalid files, malformed configs)

## Adding New Tests

1. Create a new test file in `tests/` directory (must start with `test_`)
2. Import `unittest` and the module you want to test
3. Create test class inheriting from `unittest.TestCase`
4. Write test methods (must start with `test_`)

Example:

```python
import unittest

class TestNewFeature(unittest.TestCase):
    def setUp(self):
        """Set up before each test."""
        pass

    def test_something(self):
        """Test description."""
        self.assertEqual(1 + 1, 2)
```

## Test Fixtures

Sample configurations are stored in `fixtures/sample_configs/`:
- `test_switch.txt` - Basic switch configuration for testing

To add new fixtures:
1. Create config file in `fixtures/sample_configs/`
2. (Optional) Add expected output in `fixtures/expected_outputs/`
3. Reference in your tests

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run Tests
  run: python tests/run_tests.py
```

## Best Practices

1. **Test Independence**: Each test should be independent and not rely on others
2. **Clear Names**: Use descriptive test names that explain what is being tested
3. **Single Assertion Focus**: Each test should focus on one specific behavior
4. **Use setUp/tearDown**: Initialize common test data in `setUp()`
5. **Test Edge Cases**: Don't just test happy paths, test failures too

## Interpreting Results

### Successful Test Run
```
Ran 25 tests in 2.543s

OK
✓ All tests passed!
```

### Failed Test Run
```
FAIL: test_extract_vlans (test_config_parser.TestCiscoConfigParser)
----------------------------------------------------------------------
AssertionError: 10 not found in [20, 30]

Ran 25 tests in 2.102s
FAILED (failures=1)
❌ Some tests failed.
```

## Troubleshooting

### Import Errors
If you get import errors, ensure:
- You're running from the project root directory
- The automation module is in the correct path
- All dependencies are installed (`pip install -r requirements.txt`)

### Test Data Not Found
If fixtures are missing:
- Ensure `fixtures/sample_configs/test_switch.txt` exists
- Check file paths in test code
- Verify test is running from correct directory

## Contributing

When adding new features:
1. Write tests FIRST (Test-Driven Development)
2. Ensure all existing tests still pass
3. Aim for >80% code coverage
4. Document new test files in this README
