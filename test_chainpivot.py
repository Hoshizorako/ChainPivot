# test_chainpivot.py
"""
Tests for ChainPivot module.
"""

import unittest
from chainpivot import ChainPivot

class TestChainPivot(unittest.TestCase):
    """Test cases for ChainPivot class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainPivot()
        self.assertIsInstance(instance, ChainPivot)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainPivot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
