# Installation

## System Requirements

RIDE CLI supports Python 3.8+ and runs on:
- 🐧 Linux
- 🍎 macOS
- 🪟 Windows

## Installation Methods

### Using pip (Recommended)

```bash
pip install ride-cli
```

### From Source

```bash
git clone https://github.com/sudhanshumukherjeexx/ride-cli.git
cd ride-cli
pip install -e .
```

### Development Installation

For contributors:

```bash
git clone https://github.com/sudhanshumukherjeexx/ride-cli.git
cd ride-cli
pip install -e ".[dev,docs]"
```

## Virtual Environment (Recommended)

We recommend using a virtual environment to avoid dependency conflicts:

### Linux/macOS

```bash
python3 -m venv ride-env
source ride-env/bin/activate
pip install ride-cli
```

### Windows

```bash
python -m venv ride-env
ride-env\Scripts\activate
pip install ride-cli
```

## Verifying Installation

After installation, verify RIDE is working:

```bash
ride --version
```

## Dependencies

RIDE CLI automatically installs these key dependencies:
- pandas
- numpy
- scikit-learn
- matplotlib
- plotext
- termcolor
- pyfiglet

## Troubleshooting

### Common Issues

- **Command not found**: Make sure your Python Scripts directory is in PATH
- **Permission denied**: Use `--user` flag or run in a virtual environment
- **Dependency conflicts**: Create a fresh virtual environment

## Getting Help

If you encounter issues:
- Check the [GitHub Issues](https://github.com/sudhanshumukherjeexx/ride-cli/issues)
- Create a new issue with your error message