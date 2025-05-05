# Release Process Guide

This document outlines the complete manual process for releasing new versions of RIDE CLI.

## Version Numbering

RIDE CLI follows [Semantic Versioning](https://semver.org/) (SemVer):

- **MAJOR** version (X.0.0): Incompatible API changes, major feature changes
- **MINOR** version (0.X.0): New functionality added in a backward compatible manner
- **PATCH** version (0.0.X): Backward compatible bug fixes

## Pre-Release Checklist

Before starting the release process, verify:

- [ ] All tests pass (`pytest -v`)
- [ ] Documentation is up-to-date
- [ ] CHANGELOG.md is updated with all changes
- [ ] All GitHub issues for this milestone are closed or moved
- [ ] Code quality checks pass (`flake8`, `black`, `isort`)
- [ ] All dependencies are pinned to specific versions

## Step 1: Update Version Numbers

Manually update version numbers in these files:

1. **ride/__init__.py**:
   ```python
   __version__ = "0.3.1"  # Update to new version
   ```

2. **setup.py**:
   ```python
   version="0.3.1",  # Update to new version
   ```

3. **pyproject.toml**:
   ```toml
   version = "0.3.1"  # Update to new version
   ```

## Step 2: Update CHANGELOG.md

Add a new entry at the top of the CHANGELOG.md file:

```markdown
## [0.3.1] - YYYY-MM-DD

### Added
- List of new features

### Changed
- List of changes in existing functionality

### Deprecated
- List of features that will be removed in future releases

### Removed
- List of removed features

### Fixed
- List of bug fixes

### Security
- List of security fixes
```

Make sure to:
- Use today's date
- Group changes by type
- Be specific about changes
- Reference GitHub issues when applicable (e.g., "Fixed crash when loading CSV files (#123)")

## Step 3: Commit Version Changes

```bash
# Stage all changed files
git add ride/__init__.py setup.py pyproject.toml CHANGELOG.md

# Create a commit
git commit -m "Release v0.3.1"
```

## Step 4: Create a Git Tag

```bash
# Create an annotated tag
git tag -a v0.3.1 -m "Release v0.3.1"
```

## Step 5: Push to GitHub

```bash
# Push the commit
git push origin main

# Push the tag
git push origin v0.3.1
```

## Create GitHub Release

1. Go to https://github.com/sudhanshumukherjeexx/ride-cli/releases
2. Click "Draft a new release"
3. Select the tag you created (v0.3.1)
4. Title: "RIDE CLI v0.3.1"
5. Description: Copy release notes from CHANGELOG.md
6. Attach the built packages from the `dist/` directory
7. Click "Publish release"

## Update Documentation

If using GitHub Pages with MkDocs:

```bash
# Build and deploy documentation
mkdocs gh-deploy --force
```

If manually deploying documentation, update the documentation site with:

```bash
# Build documentation

mkdocs build # Deploy to your documentation hosting service

```

## Post-Release

1. Verify the package is available on PyPI: https://pypi.org/project/ride-cli/
2. Verify documentation is updated
3. Update project roadmap if necessary
4. Create new milestone for next version on GitHub (if applicable)


### GitHub Release Issues

**Problem**: Tag already exists  
**Solution**: Delete the existing tag and create a new one
```bash
git tag -d v0.3.1
git push origin :refs/tags/v0.3.1
git tag -a v0.3.1 -m "Release v0.3.1"
git push origin v0.3.1
```

**Problem**: Upload fails  
**Solution**: Ensure your GitHub token has appropriate permissions


## Documentation

For each release, update:

1. Installation instructions with new version
2. API documentation for changed interfaces
3. User guides for new features
4. Migration guides for breaking changes


## Quick Release Reference

For experienced maintainers, here's a quick reference:

```bash
# 1. Update versions:
# - ride/__init__.py
# - setup.py
# - pyproject.toml

# 2. Update CHANGELOG.md

# 3. Commit and tag
git add .
git commit -m "Release v0.3.1"
git tag -a v0.3.1 -m "Release v0.3.1"

# 4. Push
git push origin main
git push origin v0.3.1


# 5. Create GitHub release
git push origin main
git push origin v0.3.1


# 6. Deploy docs
mkdocs gh-deploy --force
```