# RIDE CLI Interface Guide

RIDE CLI provides an intuitive, menu-driven interface for data analysis. This guide covers all interface elements and navigation.

## Interface Overview

### Start Screen

When you launch RIDE CLI, you'll see:

```
===============================================================================
                                                                               
    8888888b.  8888888 8888888b.  8888888888      .d8888b.  888      8888888  
    888   Y88b   888   888  "Y88b 888            d88P  Y88b 888        888    
    888    888   888   888    888 888            888    888 888        888    
    888   d88P   888   888    888 8888888        888        888        888    
    8888888P"    888   888    888 888            888        888        888    
    888 T88b     888   888    888 888            888    888 888        888    
    888  T88b    888   888  .d88P 888            Y88b  d88P 888        888    
    888   T88b 8888888 8888888P"  8888888888      "Y8888P"  88888888 8888888  
                                                                               
===============================================================================

RIDE: Rapid Insights Data Engine

RIDE is a free open-source toolkit that lets you perform data analysis
without writing a single line of code and minimal intervention.

===============================================================================
```

### Main Menu

The main menu provides access to all features:

```
Main Menu:

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

'$' Export Data (saves current state)
'exit': Exit RIDE CLI

Enter your choice (1-10, $, exit):
```

## Navigation

### Menu Navigation
- Enter the number (1-10) to select an option
- Type '$' for quick export
- Type 'exit' to quit the application
- Press Enter after each selection

### Submenu Navigation
- Each main option has its own submenu
- Navigate back to the main menu by selecting the "Back" option
- Most submenus are numbered similarly to the main menu

## Section Headers

RIDE CLI uses dynamic section headers that adapt to your terminal size:

```
╔═════════════════════════════════════════════════════════════════════════════╗
║                               Load Dataset                                  ║
║ ─────────────────────────────────────────────────────────────────────────── ║
║           Import your data from CSV, Excel, or Parquet files                ║
╚═════════════════════════════════════════════════════════════════════════════╝

Current dataset: iris.csv
Shape: 150 rows × 5 columns
────────────────────────────────────────────────────────────────────────────────
```

## Menu Options Detail

### 1. Load Dataset Menu

```
Options:
1. Load your own data
2. Load default data (Pre-loaded)
0. Back to main menu

Enter your choice (0-2):
```

When loading default data:
```
📊 Default Datasets Available:
--------------------------------------------------------------------------------
1. ames_housing.csv
   House prices in Ames, Iowa with 82 features about property characteristics.

2. camera_dataset.csv
   Digital camera specifications including resolution, zoom, dimensions.

3. Fish.csv
   Fish species measurements including weight, length, height, and width.

4. penguins.csv
   Palmer Penguins dataset with penguin species measurements.

5. titanic.csv
   Titanic passengers data with survival information and demographics.
--------------------------------------------------------------------------------
0. Back to dataset loading options

Select a dataset (0-5):
```

### 2. Inspect Data Menu

```
Inspection Options:
1. View features and data types
2. View dataset shape
3. Check missing values
4. View data sample
5. View summary statistics
6. Back to main menu

Enter your choice (1-6):
```

### 3. Data Type Conversion

Shows columns with interactive selection:
```
Columns available for data type conversion:
-----------------------------------------------------------------------------------
#   Column Name                    Current Type    Sample Values
-----------------------------------------------------------------------------------
1   sepal_length                   float64        5.1, 4.9, 4.7
2   sepal_width                    float64        3.5, 3.0, 3.2
3   species                        object         setosa, setosa, setosa
-----------------------------------------------------------------------------------

Select columns to convert:
(Enter column numbers separated by commas)
```

### 4. Explore Data Menu

```
Exploration Options:
1. Feature correlation analysis
2. Check for normal distribution
3. Detect outliers
4. View skewness
5. View kurtosis
6. Check for imbalanced target variable
7. Back to main menu

Enter your choice (1-7):
```

### 5. Visualize Data Menu

```
Visualization Options:
1. Plot histogram
2. Plot scatter plot
3. Back to main menu

Enter your choice (1-3):
```

### 6. Impute Missing Values

```
Choice Available to Impute Missing Data:

1. [Press 1] Drop Missing Data.
2. [Press 2] Impute Missing Data with Specific Value.
3. [Press 3] Impute Missing Data with Mean.
4. [Press 4] Impute Missing Data with Median.
5. [Press 5] Impute Missing Data based on Distribution of each Feature.
6. [Press 6] Impute Missing Data with Fill Forward Strategy.
7. [Press 7] Impute Missing Data with Backward Fill Strategy.
8. [Press 8] Impute Missing Data with Nearest Neighbours.

Enter your choice:
```

### 7. Feature Encoding Menu

```
Categorical columns available in the dataset:
--------------------------------------------------------------------------------
#   Column Name                    Data Type    Unique Values    Sample Values
--------------------------------------------------------------------------------
1   species                        object       3                setosa, versi...
--------------------------------------------------------------------------------

Encoding Methods:
1. Label Encoding - Maps each unique value to a number
2. One Hot Encoding - Creates binary columns for each category
3. Ordinal Encoding - Maps values to ordered integers based on specified order
4. Exit and return to main menu

Select encoding method (1-4):
```

### 8. Feature Scaling Menu

```
Available Options:

=== SCALING OPTIONS ===
1. Min-Max Scaler [Scales features to a range of [0,1]]
2. Standard Scaler (Z-score) [Scales to mean=0, std=1]
3. Robust Scaler [Recommended if outliers are present]
4. Max Abs Scaler [Scales by dividing by the maximum absolute value]

=== TRANSFORMATION OPTIONS ===
5. Quantile Transformer [Maps to uniform or normal distribution]
6. Log Transformer [Natural logarithm transformation]
7. Reciprocal Transformation [1/x transformation]
8. Square Root Transformation [√x transformation]
=============================================================================================
9. Exit and return to main menu

Enter your choice (1-9):
```

### 9. Export Data

```
Enter the path to save the file: 

Export Format Options:
1. CSV (.csv)
2. Excel (.xlsx)
3. Parquet (.parquet)

Choose export format (1-3):
```

### 10. AutoML Interface

```
Available columns:
1. sepal_length
2. sepal_width
3. petal_length
4. petal_width
5. species

Enter the number of the target column:

Select task type:
1. Classification (target variable has discrete classes)
2. Regression (target variable has continuous values)

Enter your choice (1-2):
```

## Visual Elements

### Color Coding

RIDE CLI uses colors to enhance readability:

- 🟢 **Green**: Success messages, headers
- 🔴 **Red**: Error messages, warnings
- 🟡 **Yellow**: Important notices, section titles
- 🔵 **Blue**: Information, positive correlations
- ⚪ **White**: Standard text
- 🟦 **Cyan**: Borders, decorative elements

### Progress Indicators

During AutoML and data processing:
```
🔍 Preprocessing: Missing Value Analysis
🔀 Data Split:
🔍 Evaluating Random Forest Classifier...
✓ Completed - Balanced Accuracy: 1.0000
```

### Tables and Data Display

Data is displayed in formatted tables:
```
Top Correlations (excluding self-correlations):
------------------------------------------------------------
Feature Pair                    Correlation     Strength
------------------------------------------------------------
petal_length-petal_width         0.963         Strong
sepal_length-petal_length        0.872         Strong
sepal_length-petal_width         0.818         Strong
------------------------------------------------------------
```

### Visualizations

Terminal-based plots using plotext:
- Histograms with ASCII characters
- Scatter plots with dots
- Bar charts for correlations
- Missing value visualizations

Example histogram:
```
Histogram: sepal_length
       
    ▓▓▓
    ▓▓▓
    ▓▓▓    ▓▓▓
    ▓▓▓    ▓▓▓    ▓▓▓
    ▓▓▓    ▓▓▓    ▓▓▓
    ▓▓▓    ▓▓▓    ▓▓▓    ▓▓▓
    ▓▓▓    ▓▓▓    ▓▓▓    ▓▓▓    ▓▓▓
    ▓▓▓    ▓▓▓    ▓▓▓    ▓▓▓    ▓▓▓
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     4.3    5.1    5.9    6.7    7.5
```

## Input Handling

### Text Input
- File paths: Can use relative or absolute paths
- Column selection: Enter numbers or "all"
- Yes/No questions: Accept 'y', 'n', 'yes', 'no' (case-insensitive)

### Numeric Input
- Menu choices: Enter single digits or numbers
- Multiple selections: Comma-separated values (e.g., "1,3,5")
- Ranges: Not supported, use comma-separated lists

### File Path Input
- Supports Windows and Unix-style paths
- Automatically converts backslashes to forward slashes
- Creates directories if they don't exist (with user confirmation)

## Error Handling

### Common Error Messages

```
❌ Error loading file: [Errno 2] No such file or directory
Invalid choice. Please try again.
No numerical columns found for scaling/transformation.
```

### Error Recovery
- Invalid inputs return to the menu
- File errors provide clear messages
- Operations can be cancelled without data loss
- Press Enter to continue after errors

## Status Messages

### Success Messages
```
✅ Successfully converted 'species' to String (object)
Success! Dataset loaded with 150 rows and 5 columns.
Features scaled and saved successfully
```

### Warning Messages
```
⚠️ Warning: Target variable has 150 unique values
No missing values found in the dataset.
Column 'price' contains zeros which cannot be reciprocally transformed.
```

## Tips for Effective Use

1. **Terminal Size**: RIDE CLI adapts to your terminal width - use a wider terminal for better visualization
2. **Quick Navigation**: Use the number keys for faster menu navigation
3. **Data Backup**: Always keep a backup of your original data
4. **Path Entry**: Use Tab completion in your terminal when entering file paths
5. **Cancel Operations**: Most operations can be cancelled by entering 'exit' or invalid input
6. **Clear Screen**: The interface automatically clears the screen between major operations

## Keyboard Shortcuts

- **Enter**: Confirm selection or continue
- **Ctrl+C**: Force quit the application (use with caution)
- **Number Keys**: Quick menu selection
- **$**: Quick export shortcut from main menu

## Interface Customization

While RIDE CLI doesn't offer built-in customization, you can:
- Adjust terminal font size for better readability
- Change terminal color scheme to improve contrast
- Resize terminal window to accommodate visualizations