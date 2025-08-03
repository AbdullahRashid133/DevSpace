# test_devspace.py
"""
Tests for DevSpace module.
"""

import unittest
from devspace import DevSpace

class TestDevSpace(unittest.TestCase):
    """Test cases for DevSpace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DevSpace()
        self.assertIsInstance(instance, DevSpace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DevSpace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
