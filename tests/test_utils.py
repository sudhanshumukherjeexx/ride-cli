"""Tests for utils module functionality"""

import pytest
import pandas as pd
import numpy as np
from ride.utils import Prepup


class TestPrepup:
    @pytest.fixture
    def sample_df(self):
        """Create a sample dataframe for testing"""
        return pd.DataFrame({
            'numeric': [1, 2, 3, 4, 5],
            'categorical': ['A', 'B', 'A', 'B', 'C'],
            'with_missing': [1, np.nan, 3, np.nan, 5]
        })
    
    def test_init(self, sample_df):
        """Test Prepup initialization"""
        processor = Prepup(sample_df)
        assert processor.dataframe.equals(sample_df)
    
    def test_features_available(self, sample_df):
        """Test features_available method"""
        processor = Prepup(sample_df)
        features = processor.features_available()
        assert features.tolist() == ['numeric', 'categorical', 'with_missing']
    
    def test_shape_data(self, sample_df):
        """Test shape_data method"""
        processor = Prepup(sample_df)
        shape = processor.shape_data()
        assert shape == (5, 3)
    
    def test_missing_values_count(self, sample_df):
        """Test missing_values_count method"""
        processor = Prepup(sample_df)
        missing = processor.missing_values_count()
        assert missing['with_missing'] == 2
        assert missing['numeric'] == 0
        assert missing['categorical'] == 0
    
    def test_dtype_features(self, sample_df):
        """Test dtype_features method"""
        processor = Prepup(sample_df)
        dtypes = processor.dtype_features()
        assert dtypes['numeric'] == 'int64'
        assert dtypes['categorical'] == 'object'
        assert dtypes['with_missing'] == 'float64'
    
    def test_skewness(self, sample_df):
        """Test skewness calculation"""
        processor = Prepup(sample_df)
        # This should not raise an error
        processor.skewness()
    
    def test_kurtosis(self, sample_df):
        """Test kurtosis calculation"""
        processor = Prepup(sample_df)
        # This should not raise an error
        processor.kurtosis()