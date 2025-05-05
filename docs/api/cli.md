# CLI API Reference

The `cli.py` module provides the main command-line interface for RIDE CLI.

## Classes

### `RideInteractive`

The main class that handles the interactive CLI interface.

```python
class RideInteractive:
    def __init__(self)
```

#### Attributes

- `dataframe`: pandas.DataFrame or None - The current working dataset
- `file_path`: str or None - Path to the currently loaded file
- `data_processor`: Prepup or None - Instance of the data processing utility
- `term_font`: Figlet - Terminal font for ASCII art
- `big_font`: Figlet - Large font for headers

#### Methods

##### `display_section_header(title, subtitle=None)`
Displays a formatted section header that adjusts to screen size.

**Parameters:**
- `title`: str - Main title for the section
- `subtitle`: str, optional - Additional description text

**Example:**
```python
self.display_section_header(
    "Data Exploration",
    "Perform statistical analysis and discover patterns in your data"
)
```

##### `display_header()`
Displays the main application header with ASCII art logo.

##### `display_formatted_description()`
Displays a properly formatted description that adjusts to screen size.

##### `load_data()`
Interactive method to load datasets from files or pre-loaded options.

**Features:**
- Supports CSV, Excel (.xlsx, .xls), and Parquet files
- Provides access to 5 pre-loaded datasets
- Handles file loading errors gracefully

##### `inspect_data()`
Provides data inspection options including:
1. View features and data types
2. View dataset shape
3. Check missing values
4. View data sample
5. View summary statistics

##### `explore_data()`
Offers statistical analysis options:
1. Feature correlation analysis
2. Check for normal distribution
3. Detect outliers
4. View skewness
5. View kurtosis
6. Check for imbalanced target variable

##### `visualize_data()`
Creates terminal-based visualizations:
1. Plot histogram
2. Plot scatter plot

##### `impute_missing_values()`
Handles missing values with multiple strategies:
1. Drop missing data
2. Impute with specific value
3. Impute with mean
4. Impute with median
5. Impute based on distribution
6. Forward fill strategy
7. Backward fill strategy
8. Nearest neighbors imputation

##### `standardize_features()`
Applies feature scaling and transformation methods.

##### `encode_features()`
Encodes categorical variables using various methods.

##### `change_datatype()`
Converts column data types interactively.

##### `export_data()`
Exports data to various formats:
- CSV (.csv)
- Excel (.xlsx)
- Parquet (.parquet)

##### `automl()`
Runs AutoML to find the best model for classification or regression tasks.

**Parameters taken interactively:**
- Target column selection
- Task type (classification/regression)
- Output file path

##### `run()`
Main loop that runs the interactive interface.

##### `display_no_data_message()`
Displays a message when no dataset is loaded.

## Functions

### `load_file(file_path)`
Loads a file based on its extension.

**Parameters:**
- `file_path`: str - Path to the file to load

**Returns:**
- pandas.DataFrame - Loaded dataset

**Raises:**
- ValueError: If file format is not supported

**Supported formats:**
- CSV (.csv)
- Excel (.xlsx)
- Parquet (.parquet)

### `main()`
Main entry point for the CLI application.

**Features:**
- Sets up stdout encoding for UTF-8
- Parses command-line arguments
- Initializes the interactive interface
- Handles optional file loading from command line

## Command Line Usage

### Basic Usage

```bash
# Start interactive mode
ride

# Load a file directly
ride path/to/dataset.csv
```

### Arguments

- `file`: Optional positional argument - Path to dataset file to load on startup

## Error Handling

The CLI includes comprehensive error handling for:
- File loading errors
- Invalid user inputs
- Data processing errors
- Missing data issues
- Invalid file formats

## Color Coding

The CLI uses the following color scheme:
- Green: Success messages, headers
- Red: Error messages
- Yellow: Warning messages, section titles
- Blue: Information, data values
- Cyan: Decorative borders

## Dependencies

Required packages:
- pandas
- numpy
- plotext
- termcolor
- pyfiglet
- sklearn

## Example Usage

```python
from ride.cli import RideInteractive, main

# Create interactive interface
app = RideInteractive()

# Load a dataset
app.file_path = "data/iris.csv"
app.dataframe = pd.read_csv(app.file_path)

# Run the interface
app.run()

# Or use the main function
if __name__ == "__main__":
    main()
```

## Integration with Other Modules

The CLI integrates with:
- `utils.Prepup`: For data processing operations
- `automl_processor.AutoMLProcessor`: For automatic machine learning