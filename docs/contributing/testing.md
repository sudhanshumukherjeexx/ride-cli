# Testing Guide

This guide describes how to run and develop tests for the RIDE CLI project.

## Overview

RIDE CLI uses pytest for testing various components of the application:

- **Basic Tests**: Ensures the package can be imported correctly
- **CLI Tests**: Tests the command-line interface functionality
- **Utils Tests**: Validates the data processing utilities
- **AutoML Tests**: Verifies machine learning pipeline operations

## Running Tests

To run the full test suite:

```bash
# Install testing dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage report
pytest --cov=ride
```

To run specific test files:

```bash
# Run specific test modules
pytest tests/test_basic.py
pytest tests/test_cli.py
pytest tests/test_utils.py
pytest tests/test_automl.py
```

## Test Structure

Each module in RIDE CLI has corresponding test files:

| Module | Test File | Tests |
|--------|-----------|-------|
| Package | `test_basic.py` | Basic import functionality, version check |
| CLI | `test_cli.py` | Interface initialization, file loading, integration |
| Utils | `test_utils.py` | Data processing utilities, statistics functions |
| AutoML | `test_automl.py` | ML model training and evaluation |

## Writing New Tests

When adding new features to RIDE CLI, please include corresponding tests:

1. Add tests to the appropriate test file or create a new one if needed
2. Use pytest fixtures for setting up test data
3. Follow the existing naming conventions (`test_*`)
4. Document test functions with docstrings

Example test function:

```python
def test_new_feature(sample_data):
    """Test description explaining what is being tested"""
    # Test setup
    processor = SomeProcessor(sample_data)
    
    # Execute feature
    result = processor.new_feature()
    
    # Assert expected outcomes
    assert result is not None
    assert isinstance(result, ExpectedType)
```

## Test Fixtures

The test suite uses fixtures to provide common test data:

- `sample_df`: Basic dataframe with numeric, categorical, and missing values
- `sample_classification_data`: Dataset for testing classification models
- `sample_regression_data`: Dataset for testing regression models

Use these fixtures in your tests to maintain consistency.

## Continuous Integration

Tests are automatically run on every pull request and push to the main branch through GitHub Actions. The CI pipeline:

1. Sets up Python environment
2. Installs dependencies
3. Runs tests with coverage reporting
4. Fails if tests don't pass or coverage drops below threshold

