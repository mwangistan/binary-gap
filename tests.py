import unittest
from binary import binary_gap

class TestBinaryGap(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(5, binary_gap(1041))

    def test_example2(self):
        self.assertEqual(0, binary_gap(15))

    def test_extremes(self):
        self.assertEqual(0, binary_gap(1))
        self.assertEqual(1, binary_gap(5))

    def test_trailing_zeros(self):
        self.assertEqual(binary_gap(6), 0)
        self.assertEqual(binary_gap(328), 2)

    def test_simple1(self):
        self.assertEqual(binary_gap(9), 2)
        self.assertEqual(binary_gap(11), 1)

    def test_simple2(self):
        self.assertEqual(binary_gap(19), 2)
        self.assertEqual(binary_gap(42), 1)

    def test_simple3(self):
        self.assertEqual(binary_gap(1162), 3)
        self.assertEqual(binary_gap(5), 1)

    def test_medium1(self):
        self.assertEqual(binary_gap(51712), 2)
        self.assertEqual(binary_gap(20), 1)

    def test_medium2(self):
        self.assertEqual(binary_gap(561892), 3)
        self.assertEqual(binary_gap(9), 2)

    def test_medium3(self):
        self.assertEqual(binary_gap(66561), 9)

    def test_large1(self):
        self.assertEqual(binary_gap(6291457), 20)

    def test_large2(self):
        self.assertEqual(binary_gap(74901729), 4)

    def test_large3(self):
        self.assertEqual(binary_gap(805306369), 27)

    def test_large4(self):
        self.assertEqual(binary_gap(1376796946), 5)

    def test_large5(self):
        self.assertEqual(binary_gap(1073741825), 29)

    def test_large6(self):
        self.assertEqual(binary_gap(1610612737), 28)

if __name__ == '__main__':
    unittest.main()