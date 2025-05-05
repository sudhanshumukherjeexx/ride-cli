# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2025-05-04

### Added
- Comprehensive test suite for core functionality
- Test coverage for AutoML processor, CLI interface, and utilities
- Automated testing workflow with pytest
- Test fixtures for better test isolation

### Fixed
- Fixed `missing_values_count` method in utils.py (empty property was incorrectly called as method)
- Fixed stdout handling in CLI to prevent test failures
- Fixed import issues in test files

### Changed
- Added openpyxl as a dependency for Excel file support in tests

### Developer Notes
- All tests now passing successfully (21 tests)
- Fixed pytest compatibility issues with stdout modification
- Improved test isolation using fixtures

## [0.3.0] - 2025-05-04

### Changed
- **BREAKING**: Renamed package from `prepup-linux` to `ride-cli`
- Rebranded from "Prepup" to "RIDE" (Rapid Insights Data Engine) CLI
- Updated command from `prepup` to `ride` (with `ride-cli` as alternative)  
- Renamed internal module from `main` to `ride`
- Renamed main entry point from `run.py` to `cli.py`
- Updated all internal references and imports
- Enhanced user interface with new branding

### Added
- Cross-platform support messaging (no longer implies Linux-only)
- Alternative command `ride-cli` for consistency with package name
- Migration instructions in README
- Modern packaging configuration with pyproject.toml

### Fixed
- Misleading package name that suggested Linux-only support