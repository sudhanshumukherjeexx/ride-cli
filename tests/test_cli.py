"""Tests for RIDE CLI interface"""

import pytest
import pandas as pd
from ride.cli import RideInteractive, load_file
from ride.utils import Prepup


class TestRideCLI:
    def test_interactive_init(self):
        """Test RideInteractive initialization"""
        app = RideInteractive()
        assert app.dataframe is None
        assert app.file_path is None
        assert app.data_processor is None
    
    def test_load_file_csv(self, tmp_path):
        """Test CSV file loading"""
        # Create a test CSV file
        test_file = tmp_path / "test.csv"
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df.to_csv(test_file, index=False)
        
        # Load the file
        loaded_df = load_file(str(test_file))
        assert loaded_df.equals(df)
    
    def test_load_file_excel(self, tmp_path):
        """Test Excel file loading"""
        # Create a test Excel file
        test_file = tmp_path / "test.xlsx"
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df.to_excel(test_file, index=False)
        
        # Load the file
        loaded_df = load_file(str(test_file))
        assert loaded_df.equals(df)
    
    def test_load_file_parquet(self, tmp_path):
        """Test Parquet file loading"""
        # Create a test Parquet file
        test_file = tmp_path / "test.parquet"
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df.to_parquet(test_file)
        
        # Load the file
        loaded_df = load_file(str(test_file))
        assert loaded_df.equals(df)
    
    def test_load_file_invalid_extension(self):
        """Test invalid file extension"""
        with pytest.raises(ValueError, match="Invalid file format"):
            load_file("test.txt")
    
    def test_data_processor_integration(self):
        """Test integration with Prepup data processor"""
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        processor = Prepup(df)
        
        # Test basic functionality
        assert processor.features_available().tolist() == ['A', 'B']
        assert processor.shape_data() == (3, 2)