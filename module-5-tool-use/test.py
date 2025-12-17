import unittest
from main import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test suite for the calculate_pi function"""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated correctly to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159  # Pi to 5 decimal places
        self.assertEqual(result, expected)
    
    def test_pi_to_2_digits(self):
        """Test that pi is calculated correctly to 2 decimal places"""
        result = calculate_pi(2)
        expected = 3.14
        self.assertEqual(result, expected)
    
    def test_pi_to_3_digits(self):
        """Test that pi is calculated correctly to 3 decimal places"""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected)
    
    def test_pi_to_10_digits(self):
        """Test that pi is calculated correctly to 10 decimal places"""
        result = calculate_pi(10)
        expected = 3.1415926536  # Pi to 10 decimal places
        self.assertEqual(result, expected)
    
    def test_pi_is_float(self):
        """Test that the result is a float"""
        result = calculate_pi(5)
        self.assertIsInstance(result, float)
    
    def test_pi_is_positive(self):
        """Test that pi is positive"""
        result = calculate_pi(5)
        self.assertGreater(result, 0)
    
    def test_pi_in_expected_range(self):
        """Test that pi is in the expected range"""
        result = calculate_pi(5)
        self.assertGreater(result, 3.14)
        self.assertLess(result, 3.15)


if __name__ == '__main__':
    # Run the tests
    unittest.main()
