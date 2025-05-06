# Development Guide

This guide provides information for developers who want to contribute to RIDE CLI.

## Setting Up Development Environment

### Prerequisites

- Python 3.10 or higher
- Git
- pip
- Virtual environment (venv or conda)

### Installation for Development

1. Clone the repository:
   ```bash
   git clone https://github.com/sudhanshumukherjeexx/ride-cli.git
   cd ride-cli
   ```

2. Create and activate a virtual environment:
   ```bash
   # Using venv
   python -m venv ride-env
   
   # On Windows
   ride-env\Scripts\activate
   
   # On macOS/Linux
   source ride-env/bin/activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev,docs]"
   ```

## Project Structure

```
ride-cli/
├── ride/                   # Main package
│   ├── __init__.py         # Package initialization
│   ├── cli.py              # Command line interface
│   ├── utils.py            # Utility functions
│   └── automl_processor.py # AutoML functionality
├── datasets/               # Default datasets
├── tests/                  # Test suite
├── docs/                   # Documentation
├── setup.py                # Package setup
├── requirements.txt        # Dependencies
└── README.md               # Project overview
```

## Development Workflow

### Branching Strategy

We use a simplified Git flow with the following branches:
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Feature branches

For new contributions:
1. Create a feature branch from `develop`
2. Develop and test your changes
3. Submit a pull request to merge into `develop`

### Coding Standards

We follow PEP 8 style guidelines for Python code. Please ensure your code adheres to these standards:

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 79 characters for code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include type hints when appropriate

### Running Tests

Run the test suite to ensure your changes don't break existing functionality:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage report
pytest --cov=ride tests/
```

## Adding New Features

When adding new features to RIDE CLI, please follow these guidelines:

### 1. Plan Your Feature

- Define the functionality clearly
- Consider how it integrates with existing features
- Determine the user interface (CLI options, menu items)

### 2. Implementation

- Follow the modular architecture
- Keep methods focused on single responsibilities
- Use appropriate error handling
- Add interactive elements consistent with existing UI

### 3. Documentation

All new features should be documented:
- Add docstrings to new classes and methods
- Update user documentation in the `docs/` directory
- Include examples of how to use the feature

### 4. Testing

- Write unit tests for new functionality
- Include edge cases and error conditions
- Ensure tests pass on all supported platforms

## Building Documentation

We use Markdown for documentation. To build the documentation site:

```bash
# Install dependencies
pip install mkdocs mkdocs-material

# Serve documentation locally
mkdocs serve

# Build documentation site
mkdocs build
```

## Releasing

Check out the detailed [release guide](release.md).

## Continuous Integration

We use GitHub Actions for CI/CD. Workflows include:

- Running tests on multiple Python versions
- Linting with flake8
- Building documentation
- Publishing releases to PyPI

## Getting Help

If you need help during development:

- Check the [existing issues](https://github.com/sudhanshumukherjeexx/ride-cli/issues)
- Join our [Discord community](https://discord.gg/example-invite)
- Contact maintainers via email

## Best Practices

### Performance Considerations

- Be mindful of memory usage with large datasets
- Use efficient pandas and numpy operations
- Consider the impact of new features on startup time

### UI Design

- Keep the terminal interface consistent
- Follow existing menu structure patterns
- Use color coding consistently
- Ensure graceful error handling

### Compatibility

- Test on multiple operating systems
- Ensure compatibility with supported Python versions
- Be careful with external dependencies

## Code Review Process

All contributions go through code review:

1. Submit a pull request
2. Automated tests run via GitHub Actions
3. Code review by maintainers
4. Address feedback and make necessary changes
5. Final approval and merge

## License

By contributing to RIDE CLI, you agree that your contributions will be licensed under the project's MIT License.