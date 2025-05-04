# 🚀 RIDE CLI: Rapid Interactive Data Exploration

![Static Badge](https://img.shields.io/badge/Built_with_%E2%99%A5%EF%B8%8F-Sudhanshu_Mukherjee-black?link=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsudhanshumukherjeexx%2F)

![Python Versions](https://img.shields.io/badge/python-3.7+-blue.svg)
[![image](https://img.shields.io/pypi/v/ride-cli.svg)](https://pypi.python.org/pypi/ride-cli)
![Static Badge](https://img.shields.io/badge/Linux-Supported-green)
![Static Badge](https://img.shields.io/badge/macOS-Supported-blue)
![Static Badge](https://img.shields.io/badge/Windows-Supported-yellow)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **📢 Notice**: This package was previously known as `prepup-linux`. If you're upgrading from `prepup-linux`, please uninstall it first before installing `ride-cli`.

## 🌟 About

**RIDE-CLI** (Rapid Insights Data Engine) is a powerful, user-friendly command-line tool designed to simplify and streamline your data analysis workflow. Whether you're a data scientist, analyst, or researcher, RIDE provides an intuitive interface for exploring, cleaning, and preparing your datasets - all from your terminal!


## ✨ Features

### 🎯 Interactive Mode
- 📊 Load datasets from various formats (CSV, Excel, Parquet)
- 🔍 Comprehensive data inspection
- 📈 Advanced data exploration
- 🧹 Missing value handling
- 📊 Feature visualization
- 🤖 Automatic Machine Learning (AutoML) model selection

### 🛠️ Key Functionalities
- Data Loading
- Data Type Conversion
- Feature Inspection
- Correlation Analysis
- Distribution Checking
- Outlier Detection
- Missing Value Imputation
- Feature Encoding
- Feature Scaling and Transformation
- Automatic Model Training

## 📦 Installation

> **⚠️ Important:** Creating a virtual environment is highly recommended when installing ride-cli.

### 🔀 Upgrading from prepup-linux

If you're currently using `prepup-linux`, please follow these steps:

```bash
# Uninstall the old package
pip uninstall prepup-linux

# Install the new package
pip install ride-cli
```

### 💡 Setting Up a Virtual Environment

#### Windows
```bash
# Create virtual environment
python -m venv ride-env

# Activate virtual environment
ride-env\Scripts\activate

# Deactivate when done
deactivate
```

#### Linux/macOS
```bash
# Create virtual environment
python3 -m venv ride-env

# Activate virtual environment
source ride-env/bin/activate

# Deactivate when done
deactivate
```

### 📥 Using pip
```bash
# Inside your activated virtual environment
pip install ride-cli
```

### 🔧 From Source
```bash
# Inside your activated virtual environment
git clone https://github.com/sudhanshumukherjeexx/ride-cli.git
cd ride-cli
pip install .
```

## 💻 Usage

### 🎮 Interactive Mode
```bash
ride
```
or
```bash
ride-cli
```

### 📂 Loading a Specific Dataset
```bash
ride path/to/your/dataset.csv
```

### 📋 Main Menu Options
1. Load Dataset
2. Inspect Data
3. Change Data Type
4. Explore Data
5. Visualize Data
6. Impute Missing Values
7. Feature Encoding
8. Feature Scaling and Transformation
9. Export Data
10. AutoML (Train & Evaluate Models)

## 🎯 Interactive Workflow Example

1. **Launch RIDE:** ```ride```

2. **Load Your Dataset:** Choose option 1 and enter your dataset path

3. **Inspect Data:** Use option 2 to explore features, data types, and missing values

4. **Preprocess:** 
   - Change data types if needed
   - Impute missing values
   - Encode categorical features
   - Scale and transform features

5. **Analyze:** 
   - Visualize data distributions
   - Perform correlation analysis
   - Run AutoML for model selection

## 🤖 AutoML Capabilities
- Supports both Classification and Regression tasks
- Evaluates multiple machine learning algorithms
- Provides performance metrics
- Saves results to CSV for further analysis

## 📊 Supported File Formats
- CSV (.csv)
- Excel (.xlsx, .xls)
- Parquet (.parquet)

## 🛠️ Dependencies
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Plotext (for terminal-based plotting)
- and more (see requirements.txt)

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🔗 Package Links

- Github: https://github.com/sudhanshumukherjeexx/ride-cli
- PyPI: https://pypi.org/project/ride-cli/
- Previous Package (prepup-linux): https://github.com/sudhanshumukherjeexx/prepup-linux

## 📜 Changelog

### v0.3.0 (2024)
- 🎉 Renamed from `prepup-linux` to `ride-cli`
- 🌍 Added cross-platform support
- ✨ Enhanced user interface
- 🔧 Improved stability and performance

## 🙏 Acknowledgments

Special thanks to all contributors and users of the previous `prepup-linux` package. Your feedback and support made this evolution possible!

---

Made with ❤️ by [Sudhanshu Mukherjee](https://github.com/sudhanshumukherjeexx)