"""Tests for AutoML processor functionality"""

import pytest
import pandas as pd
import numpy as np
from ride.automl_processor import AutoMLProcessor


class TestAutoMLProcessor:
    @pytest.fixture
    def sample_classification_data(self):
        """Create sample data for classification"""
        np.random.seed(42)
        X = np.random.randn(100, 5)
        y = np.random.randint(0, 2, 100)
        df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
        df['target'] = y
        return df
    
    @pytest.fixture
    def sample_regression_data(self):
        """Create sample data for regression"""
        np.random.seed(42)
        X = np.random.randn(100, 5)
        y = np.random.randn(100)
        df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
        df['target'] = y
        return df
    
    def test_automl_init(self, sample_classification_data):
        """Test AutoMLProcessor initialization"""
        processor = AutoMLProcessor(sample_classification_data)
        assert processor.original_df.equals(sample_classification_data)
        assert processor.preprocessed_df is None
        assert processor.X_train is None
        assert processor.X_test is None
    
    def test_classification_models(self, sample_classification_data):
        """Test classification model evaluation"""
        processor = AutoMLProcessor(sample_classification_data)
        results = processor.run_automl('target', 'classification')
        
        # Check that results contain expected metrics
        assert 'Accuracy' in results.columns
        assert 'F1 Score' in results.columns
        assert len(results) > 0  # At least one model should be evaluated
    
    def test_regression_models(self, sample_regression_data):
        """Test regression model evaluation"""
        processor = AutoMLProcessor(sample_regression_data)
        results = processor.run_automl('target', 'regression')
        
        # Check that results contain expected metrics
        assert 'R²' in results.columns
        assert 'MSE' in results.columns
        assert 'RMSE' in results.columns
        assert len(results) > 0  # At least one model should be evaluated
    
    def test_invalid_task_type(self, sample_classification_data):
        """Test invalid task type raises error"""
        processor = AutoMLProcessor(sample_classification_data)
        with pytest.raises(ValueError, match="Task type must be"):
            processor.run_automl('target', 'invalid_type')
    
    def test_invalid_target_column(self, sample_classification_data):
        """Test invalid target column raises error"""
        processor = AutoMLProcessor(sample_classification_data)
        with pytest.raises(ValueError, match="Target column .* not found"):
            processor.run_automl('non_existent_column', 'classification')