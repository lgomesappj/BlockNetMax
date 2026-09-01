# test_blocknetmax.py
"""
Tests for BlockNetMax module.
"""

import unittest
from blocknetmax import BlockNetMax

class TestBlockNetMax(unittest.TestCase):
    """Test cases for BlockNetMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockNetMax()
        self.assertIsInstance(instance, BlockNetMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockNetMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
