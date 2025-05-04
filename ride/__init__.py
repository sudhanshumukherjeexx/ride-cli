# ride/__init__.py
from .utils import Prepup  # We'll rename this class to RideProcessor in a future update
from .automl_processor import AutoMLProcessor

__version__ = "0.3.0"
__all__ = ['Prepup', 'AutoMLProcessor']