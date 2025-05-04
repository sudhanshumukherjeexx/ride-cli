# Contributing to RIDE CLI

We love your input! We want to make contributing to RIDE CLI as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with Github

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Development Process

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code follows the existing style.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project.

## Report bugs using Github's [issue tracker](https://github.com/sudhanshumukherjeexx/ride-cli/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/sudhanshumukherjeexx/ride-cli/issues/new).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sudhanshumukherjeexx/ride-cli.git
   cd ride-cli
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Run tests:
   ```bash
   pytest
   ```

5. Check code style:
   ```bash
   flake8 ride tests
   black --check ride tests
   isort --check-only ride tests
   ```

6. Format code:
   ```bash
   black ride tests
   isort ride tests
   ```

## Pull Request Process

1. Update the README.md with details of changes to the interface, if applicable.
2. Update the CHANGELOG.md with notes on your changes following the existing format.
3. The PR will be merged once you have the sign-off of at least one maintainer.


## Testing

- Write tests for any new functionality
- Ensure all tests pass before submitting a PR
- Aim for high test coverage
- Use pytest fixtures for common test data

## Documentation

- Update docstrings for any changed functionality
- Update README.md if you change user-facing features
- Add examples for new features
- Keep documentation clear and concise

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Questions?

Feel free to open an issue with your question or reach out to the maintainer.

Thank you for contributing to RIDE CLI! 🚀