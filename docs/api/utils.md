# Utils API Reference

The `utils.py` module provides data preprocessing and analysis utilities through the `Prepup` class.

## Classes

### `Prepup`

Main class for data preprocessing and analysis operations.

```python
class Prepup:
    def __init__(self, dataframe)
```

#### Parameters
- `dataframe`: pandas.DataFrame or None - The dataset to process

#### Methods

##### Data Inspection Methods

###### `features_available()`
Returns a list of features available in the dataframe.

**Returns:**
- pandas.Index - Column names

###### `dtype_features()`
Returns the data types of each feature in the dataset.

**Returns:**
- pandas.Series - Data types for each column

###### `missing_values_count()`
Returns the number of missing values in each column.

**Returns:**
- pandas.Series - Count of missing values per column

###### `shape_data()`
Returns the shape of the dataframe.

**Returns:**
- tuple - (rows, columns)

##### Visualization Methods

###### `missing_plot()`
Creates a terminal-based bar plot showing missing values for each column.

**Features:**
- Uses plotext for terminal visualization
- Only shows columns with missing values
- Displays count and visual representation

###### `plot_histogram()`
Creates an interactive histogram for a selected numerical column.

**Features:**
- Lists all numerical columns
- Interactive column selection
- Displays basic statistics (mean, median, std, min, max)
- Terminal-based visualization using plotext

###### `plot_scatter()`
Creates an interactive scatter plot for two selected numerical columns.

**Features:**
- Requires at least 2 numerical columns
- Interactive column selection for X and Y axes
- Shows correlation coefficient
- Indicates correlation strength (weak/moderate/strong)

##### Statistical Analysis Methods

###### `correlation_n()`
Analyzes correlations between numerical features.

**Features:**
- Calculates correlation matrix
- Displays unique correlations (excluding self-correlations)
- Shows correlation strength classification
- Creates bar plot visualization for correlations
- Handles large feature sets by showing top correlations

###### `check_nomral_distrubution()`
Checks if features are normally distributed using Shapiro-Wilk test.

**Features:**
- Tests each numerical column
- Reports p-values
- Indicates normal vs non-normal distribution

###### `find_outliers(k=1.5)`
Detects outliers using the IQR method.

**Parameters:**
- `k`: float - IQR multiplier for outlier detection (default: 1.5)

**Features:**
- Uses interquartile range method
- Reports outliers for each numerical column

###### `skewness()`
Calculates skewness for numerical features.

**Features:**
- Handles nullable integer types
- Reports skewness values for each column
- Includes error handling for edge cases

###### `kurtosis()`
Calculates kurtosis for numerical features.

**Features:**
- Similar to skewness method
- Reports kurtosis values for each column
- Handles data type conversions

###### `imbalanced_dataset()`
Analyzes class distribution for target variables.

**Features:**
- Interactive column selection
- Visual distribution plot
- Class imbalance detection and reporting
- Calculates imbalance ratio

##### Data Transformation Methods

###### `feature_encoding()`
Provides various encoding options for categorical variables.

**Encoding Methods:**
1. Label Encoding
2. One Hot Encoding
3. Ordinal Encoding

**Features:**
- Interactive column selection
- Handles missing values
- Saves encoded data to CSV
- Updates the working dataframe

###### `data_type_conversion()`
Converts data types of columns using pandas native conversion.

**Supported Types:**
- String (object)
- Integer (int8, int16, int32, int64)
- Float (float16, float32, float64)
- DateTime
- Boolean

**Features:**
- Interactive column selection
- Error handling for conversion issues
- Preview of converted data
- Option to update working dataframe

###### `feature_scaling()`
Applies various scaling and transformation methods.

**Scaling Options:**
1. Min-Max Scaler
2. Standard Scaler (Z-score)
3. Robust Scaler
4. Max Abs Scaler

**Transformation Options:**
5. Quantile Transformer
6. Log Transformer
7. Reciprocal Transformation
8. Square Root Transformation

**Features:**
- Column selection with drop option
- Handles edge cases (zeros, negatives)
- Saves transformed data to CSV

###### `handle_missing_values()`
Handles missing values with multiple strategies.

**Imputation Methods:**
1. Drop missing data
2. Impute with specific value
3. Impute with mean
4. Impute with median
5. Impute based on distribution
6. Forward fill strategy
7. Backward fill strategy
8. Nearest neighbors

**Features:**
- Interactive method selection
- Saves imputed data to CSV
- Creates backup in parquet format

## Usage Examples

```python
import pandas as pd
from ride.utils import Prepup

# Load data
df = pd.read_csv('data.csv')

# Initialize Prepup
prepup = Prepup(df)

# Inspect data
print(prepup.features_available())
print(prepup.shape_data())

# Check for missing values
prepup.missing_plot()

# Analyze correlations
prepup.correlation_n()

# Check for normal distribution
prepup.check_nomral_distrubution()

# Encode categorical features
prepup.feature_encoding()

# Scale features
prepup.feature_scaling()
```

## Dependencies

- pandas
- numpy
- plotext
- scipy
- sklearn
- termcolor
- pyfiglet

## Error Handling

The module includes comprehensive error handling for:
- Data type mismatches
- Missing value operations
- Statistical calculations
- File I/O operations
- User input validation

## Visual Output

All visualizations use plotext for terminal-based graphics:
- Bar charts for correlations and missing values
- Histograms for distributions
- Scatter plots for relationships
- Theme: 'matrix' and 'dark' for better visibility