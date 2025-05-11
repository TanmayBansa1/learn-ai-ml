import unittest
from main import calculate_power_four_sum

class TestMission1(unittest.TestCase):
    def test_calculate_power_four_sum(self):
        # Test case 1 from example
        nums = [3, -1, 1, 10]
        expected = 1  # Only -1 is negative: (-1)^4 = 1
        self.assertEqual(calculate_power_four_sum(nums, 4), expected)
        
        # Test case 2 from example
        nums = [9, -5, -5, -10, 10]
        expected = 11250  # (-5)^4 + (-5)^4 + (-10)^4 = 625 + 625 + 10000 = 11250
        self.assertEqual(calculate_power_four_sum(nums, 5), expected)
        
        # Additional test cases
        self.assertEqual(calculate_power_four_sum([], 0), 0)
        self.assertEqual(calculate_power_four_sum([1, 2, 3], 3), 0)  # All positive, should be 0
        self.assertEqual(calculate_power_four_sum([-2, -3], 2), 97)  # (-2)^4 + (-3)^4 = 16 + 81 = 97
        
        # Test case where count doesn't match
        self.assertEqual(calculate_power_four_sum([1, 2, 3], 4), -1)
        self.assertEqual(calculate_power_four_sum([1, 2, 3, 4, 5], 4), -1)

if __name__ == "__main__":
    unittest.main() 