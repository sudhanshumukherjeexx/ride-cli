# Quick Start Guide

Get started with RIDE CLI in minutes!

## Basic Usage

### 1. Launch RIDE

```bash
ride
```

Or load a dataset directly:

```bash
ride your-dataset.csv
```

This opens the interactive interface:

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

### 2. Load Your Data

Select option 1 to load your dataset:

```
Enter your choice (1-10, $, exit): 1

Options:
1. Load your own data
2. Load default data (Pre-loaded)
0. Back to main menu

Enter your choice (0-2): 1

Enter the path to your dataset file (CSV, Excel, Parquet): data/iris.csv

Success! Dataset loaded with 150 rows and 5 columns.

Preview of the first 5 rows:
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
```

#### Default Datasets Available

If you choose option 2, you can select from these pre-loaded datasets:
- Ames Housing: House prices with 82 features
- Camera Dataset: Digital camera specifications
- Fish: Fish species measurements
- Penguins: Palmer Penguins dataset
- Titanic: Passenger survival data

### 3. Inspect Your Data

Use option 2 to explore your dataset structure:

```
Enter your choice (1-10, $, exit): 2

Inspection Options:
1. View features and data types
2. View dataset shape
3. Check missing values
4. View data sample
5. View summary statistics
6. Back to main menu

Enter your choice (1-6): 1

Features available in the dataset:
Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], dtype='object')

Data types of features:
sepal_length     float64
sepal_width      float64
petal_length     float64
petal_width      float64
species           object
dtype: object
```

### 4. Change Data Types

Convert column data types with option 3:

```
Enter your choice (1-10, $, exit): 3

Columns available for data type conversion:
--------------------------------------------------
#   Column Name               Current Type     Sample Values
--------------------------------------------------
1   sepal_length              float64         5.1, 4.9, 4.7
2   sepal_width               float64         3.5, 3.0, 3.2
3   species                   object          setosa, setosa, setosa
--------------------------------------------------

Select data type:
1. String (object)
2. Integer (int8)
3. Integer (int64)
4. Float (float64)
5. DateTime
6. Boolean
```

### 5. Explore Your Data

Use option 4 for statistical analysis:

```
Enter your choice (1-10, $, exit): 4

Exploration Options:
1. Feature correlation analysis
2. Check for normal distribution
3. Detect outliers
4. View skewness
5. View kurtosis
6. Check for imbalanced target variable
7. Back to main menu

Enter your choice (1-7): 1

Top Correlations (excluding self-correlations):
------------------------------------------------------------
Feature Pair                    Correlation     Strength
------------------------------------------------------------
petal_length-petal_width         0.963         Strong
sepal_length-petal_length        0.872         Strong
sepal_length-petal_width         0.818         Strong
------------------------------------------------------------
```

### 6. Visualize Data

Create terminal-based visualizations with option 5:

```
Enter your choice (1-10, $, exit): 5

Visualization Options:
1. Plot histogram
2. Plot scatter plot
3. Back to main menu

Enter your choice (1-3): 1

Available numerical columns for histogram:
--------------------------------------------------
1. sepal_length
2. sepal_width
3. petal_length
4. petal_width
--------------------------------------------------

Enter the column number to plot histogram: 1

Plotting histogram for: sepal_length
[Terminal-based histogram appears]

Statistics for sepal_length:
Mean: 5.84
Median: 5.80
Std Dev: 0.83
Min: 4.30
Max: 7.90
```

### 7. Handle Missing Values

Impute missing data with option 6:

```
Enter your choice (1-10, $, exit): 6

Choice Available to Impute Missing Data:
1. [Press 1] Drop Missing Data
2. [Press 2] Impute Missing Data with Specific Value
3. [Press 3] Impute Missing Data with Mean
4. [Press 4] Impute Missing Data with Median
5. [Press 5] Impute Missing Data based on Distribution
6. [Press 6] Impute Missing Data with Fill Forward Strategy
7. [Press 7] Impute Missing Data with Backward Fill Strategy
8. [Press 8] Impute Missing Data with Nearest Neighbours

Enter your choice: 3

Enter path to save Imputed data: data/imputed_data.csv
Missing Data Imputed and saved successfully
```

### 8. Feature Encoding

Transform categorical variables with option 7:

```
Enter your choice (1-10, $, exit): 7

Categorical columns available:
--------------------------------------------------------
#   Column Name        Data Type    Unique Values    Sample Values
--------------------------------------------------------
1   species           object       3                setosa, versicolor...
--------------------------------------------------------

Encoding Methods:
1. Label Encoding - Maps each unique value to a number
2. One Hot Encoding - Creates binary columns for each category
3. Ordinal Encoding - Maps values to ordered integers
4. Exit and return to main menu

Select encoding method (1-4): 1

Mapping for column 'species':
  setosa → 0
  versicolor → 1
  virginica → 2
```

### 9. Feature Scaling

Scale numerical features with option 8:

```
Enter your choice (1-10, $, exit): 8

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
9. Exit and return to main menu

Enter your choice (1-9): 2

Enter path to save normalized/transformed data: data/scaled_data.csv
Features scaled and saved successfully
```

### 10. Run AutoML

Automatically find the best model with option 10:

```
Enter your choice (1-10, $, exit): 10

Available columns:
1. sepal_length
2. sepal_width
3. petal_length
4. petal_width
5. species

Enter the number of the target column: 5

Select task type:
1. Classification (target variable has discrete classes)
2. Regression (target variable has continuous values)

Enter your choice (1-2): 1

🤖 AutoML Model Selection 🤖
Task Type: Classification
Target Column: species

🔍 Preprocessing: Missing Value Analysis
Initial Missing Values:
(None found)

🔀 Data Split:
Training set: 120 samples
Testing set: 30 samples

🔍 Evaluating Random Forest Classifier...
✓ Completed - Balanced Accuracy: 1.0000

[More models evaluated...]

📊 Classification Model Comparison:
                    Balanced Accuracy  F1 Score  Accuracy
Model               
Random Forest                   1.000     1.000     1.000
Extra Trees                     1.000     1.000     1.000
LightGBM                        1.000     1.000     1.000
XGBoost                        0.967     0.967     0.967
Logistic Regression            0.967     0.967     0.967

Enter the full path to save the AutoML results: results/automl_results.csv
💾 Results saved to results/automl_results.csv
```

### 11. Export Data

Save your processed data with option 9 or '$':

```
Enter your choice (1-10, $, exit): 9

Enter the path to save the file: processed_data

Export Format Options:
1. CSV (.csv)
2. Excel (.xlsx)
3. Parquet (.parquet)

Choose export format (1-3): 1

Data exported successfully to processed_data.csv
```

## Tips and Tricks

- Use the '$' shortcut to quickly export your current dataset
- Press 'exit' at any time to quit RIDE CLI
- All visualizations are terminal-based using plotext
- You can load files directly when starting RIDE: `ride your-data.csv`
- Default datasets are available if you want to explore without your own data
- All operations preserve your original data; modifications are saved to new files

## Common Workflows

### Data Analysis Workflow
1. Load dataset
2. Inspect data types and missing values
3. Explore statistical properties
4. Visualize distributions
5. Handle missing values
6. Encode categorical features
7. Scale numerical features
8. Export processed data

### Machine Learning Workflow
1. Load dataset
2. Preprocess data (missing values, encoding, scaling)
3. Run AutoML to find best model
4. Export results for further analysis

## Need Help?

- Check the [User Guide](../user-guide/interface.md) for detailed instructions
- Report issues on [GitHub](https://github.com/sudhanshumukherjeexx/ride-cli/issues)
- Explore the [API Reference]for advanced usage:
    - [CLI Module Reference](../api/cli.md)
    - [Utils Module Reference](../api/utils.md)
    - [AutoML Processor Reference](../api/automl.md)