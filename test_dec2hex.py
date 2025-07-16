import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):
    def test_basic_values(self):
        # Test standard conversions
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(15), "F")
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_zero(self):
        # Test zero edge case
        self.assertEqual(decimal_to_hex(0), "0")

    def test_invalid_negative(self):
        # Test that negative input raises ValueError
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)

if __name__ == '__main__':
    unittest.main()

