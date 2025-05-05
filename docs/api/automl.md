# AutoML Processor API Reference

The `automl_processor.py` module provides automatic machine learning capabilities for classification and regression tasks.

## Classes

### `AutoMLProcessor`

Main class for automated machine learning pipeline.

```python
class AutoMLProcessor:
    def __init__(self, dataframe: pd.DataFrame)
```

#### Parameters
- `dataframe`: pandas.DataFrame - Input dataframe for processing and analysis

#### Attributes
- `original_df`: pandas.DataFrame - Copy of the original input dataframe
- `preprocessed_df`: pandas.DataFrame or None - Preprocessed dataset
- `X_train`: pandas.DataFrame or None - Training features
- `X_test`: pandas.DataFrame or None - Testing features
- `y_train`: pandas.Series or None - Training target
- `y_test`: pandas.Series or None - Testing target

#### Methods

##### `run_automl(target_column: str, task_type: str = 'classification') -> pd.DataFrame`

Main method to run the automated machine learning pipeline.

**Parameters:**
- `target_column`: str - Name of the target column
- `task_type`: str - Type of task ('classification' or 'regression')

**Returns:**
- pandas.DataFrame - Results of model evaluations with metrics

**Features:**
- Validates task type
- Preprocesses data automatically
- Splits data into train/test sets
- Evaluates multiple models
- Returns comparative results

**Example:**
```python
automl = AutoMLProcessor(df)
results = automl.run_automl('target', 'classification')
```

##### Private Methods

###### `_preprocess_data(target_column: str, task_type: str) -> Tuple[pd.DataFrame, pd.Series]`

Comprehensive data preprocessing with robust NaN handling.

**Parameters:**
- `target_column`: str - Target column name
- `task_type`: str - 'classification' or 'regression'

**Returns:**
- Tuple[pd.DataFrame, pd.Series] - Preprocessed features and target

**Preprocessing Steps:**
1. Handle missing values
2. Convert target to numeric for regression
3. Remove rows with missing target values
4. Impute missing values in features
5. Encode categorical variables
6. Scale features

###### `_split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> None`

Splits data into training and testing sets.

**Parameters:**
- `X`: pd.DataFrame - Feature matrix
- `y`: pd.Series - Target variable
- `test_size`: float - Proportion for testing (default: 0.2)

**Features:**
- Stratified split for classification (if < 10 classes)
- Random state for reproducibility
- Updates instance attributes

###### `_run_classification_models() -> pd.DataFrame`

Evaluates multiple classification models.

**Models Tested:**
1. Random Forest
2. Extra Trees
3. Logistic Regression
4. Decision Tree
5. K-Nearest Neighbors
6. Support Vector Machine
7. Naive Bayes
8. AdaBoost
9. XGBoost (if available)
10. LightGBM (if available)

**Metrics Calculated:**
- Accuracy
- Balanced Accuracy
- F1 Score
- Precision
- Recall
- ROC AUC (when possible)

**Returns:**
- pandas.DataFrame - Comparative results sorted by Balanced Accuracy

###### `_run_regression_models() -> pd.DataFrame`

Evaluates multiple regression models.

**Models Tested:**
1. Random Forest
2. Extra Trees
3. Linear Regression
4. Ridge Regression
5. Lasso Regression
6. Elastic Net
7. Decision Tree
8. K-Nearest Neighbors
9. Support Vector Regression
10. AdaBoost
11. XGBoost (if available)
12. LightGBM (if available)

**Metrics Calculated:**
- R²
- Adjusted R²
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)

**Returns:**
- pandas.DataFrame - Comparative results sorted by Adjusted R²

## Functions

### `example_automl_usage(csv_path: str, target_column: str, task_type: str = 'classification')`

Demonstrates AutoML usage with a CSV file.

**Parameters:**
- `csv_path`: str - Path to the input CSV file
- `target_column`: str - Name of the target column
- `task_type`: str - 'classification' or 'regression' (default: 'classification')

**Features:**
- Loads CSV file
- Initializes AutoML processor
- Runs AutoML pipeline
- Saves results to CSV
- Handles errors gracefully

**Example:**
```python
example_automl_usage('data.csv', 'target', 'classification')
```

## Model Evaluation Details

### Classification Metrics

1. **Accuracy**: Overall correct predictions
2. **Balanced Accuracy**: Average recall per class
3. **F1 Score**: Harmonic mean of precision and recall
4. **Precision**: True positives / (True positives + False positives)
5. **Recall**: True positives / (True positives + False negatives)
6. **ROC AUC**: Area under ROC curve (binary or multiclass)

### Regression Metrics

1. **R²**: Coefficient of determination
2. **Adjusted R²**: R² adjusted for number of predictors
3. **MSE**: Mean Squared Error
4. **RMSE**: Root Mean Squared Error
5. **MAE**: Mean Absolute Error
6. **MAPE**: Mean Absolute Percentage Error

## Data Preprocessing Pipeline

1. **Missing Value Analysis**
   - Reports initial missing values
   - Removes rows with missing target values
   - Imputes missing values in features

2. **Feature Type Handling**
   - Identifies numeric and categorical columns
   - Applies appropriate imputation strategies

3. **Categorical Encoding**
   - One-hot encoding for low cardinality (≤ 10 unique values)
   - Label encoding for moderate cardinality (≤ 50 unique values)
   - Drops high cardinality columns

4. **Feature Scaling**
   - Standard scaling for all numeric features
   - Preserves column names and indices

## Error Handling

The module includes error handling for:
- Invalid target column
- Data type conversion errors
- Model fitting failures
- Missing library dependencies
- File I/O errors

## Optional Dependencies

- **XGBoost**: Advanced gradient boosting
- **LightGBM**: Light gradient boosting machine

These libraries are optional and will be used if available.

## Usage Example

```python
import pandas as pd
from ride.automl_processor import AutoMLProcessor

# Load your data
df = pd.read_csv('your_data.csv')

# Initialize AutoML processor
automl = AutoMLProcessor(df)

# Run AutoML for classification
results = automl.run_automl('target_column', 'classification')

# View results
print(results)

# Save results
results.to_csv('automl_results.csv')
```

## Performance Considerations

- The preprocessing pipeline handles datasets with mixed data types
- Automatic handling of categorical variables based on cardinality
- Stratified splitting for balanced classification datasets
- Parallel model evaluation where supported by underlying libraries
- Memory-efficient preprocessing with in-place operations where possible

## Output Format

Results are returned as a pandas DataFrame with:
- Index: Model names
- Columns: Performance metrics
- Sorted by primary metric (Balanced Accuracy or Adjusted R²)

Example output:

```
📊 Classification Model Comparison:

                     Accuracy  Balanced Accuracy  F1 Score  Precision    Recall   ROC AUC
Model                                                                                    
SVM                  0.940299           0.939840  0.940219   0.941823  0.940299  0.959893
Extra Trees          0.925373           0.925134  0.925340   0.925720  0.925373  0.962121
Random Forest        0.910448           0.909537  0.910047   0.916245  0.910448  0.949198
Logistic Regression  0.910448           0.909537  0.910047   0.916245  0.910448  0.953654
LightGBM             0.910448           0.909537  0.910047   0.916245  0.910448  0.943850
Decision Tree        0.895522           0.894831  0.895242   0.898588  0.895522  0.894831
KNN                  0.880597           0.880125  0.880437   0.881854  0.880597  0.926025
AdaBoost             0.865672           0.864528  0.864767   0.873736  0.865672  0.940285
Naive Bayes          0.701493           0.700535  0.700155   0.703876  0.701493  0.858289
```


```
📊 Regression Model Comparison:
                         R²        MSE      RMSE       MAE      MAPE  Adjusted R²
Model                                                                            
Ridge Regression   0.858259   3.738288  1.933465  1.420402  0.033227     0.833821
Linear Regression  0.857912   3.747438  1.935830  1.419027  0.033188     0.833414
SVR                0.848365   3.999225  1.999806  1.542758  0.036247     0.822222
LightGBM           0.830124   4.480322  2.116677  1.641753  0.037996     0.800835
KNN                0.813527   4.918070  2.217672  1.706957  0.039691     0.781376
AdaBoost           0.812594   4.942659  2.223209  1.736601  0.039801     0.780283
Random Forest      0.805153   5.138925  2.266920  1.774667  0.041109     0.771558
Elastic Net        0.774345   5.951451  2.439560  1.922946  0.044926     0.735439
XGBoost            0.768700   6.100328  2.469884  1.888304  0.043739     0.728821
Extra Trees        0.766232   6.165434  2.483029  1.941652  0.044976     0.725927
Lasso Regression   0.753465   6.502142  2.549930  2.014548  0.046989     0.710959
Decision Tree      0.530831  12.373913  3.517657  2.747826  0.064468     0.449940
```
