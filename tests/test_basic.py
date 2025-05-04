"""Basic tests to ensure the package can be imported"""

def test_import():
    """Test that the package can be imported"""
    import ride
    assert ride.__version__ == "0.3.0"

def test_cli_import():
    """Test that the CLI module can be imported"""
    from ride import cli
    assert hasattr(cli, 'main')

def test_common_import():
    """Test that the common module can be imported"""
    from ride import utils
    assert hasattr(utils, 'Prepup')