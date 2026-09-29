import unittest
from factorial import factorial, factorial_recursive


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_small_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_large_number(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_non_integer_raises(self):
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_recursive_matches_iterative(self):
        for n in range(0, 15):
            self.assertEqual(factorial(n), factorial_recursive(n))

    def test_recursive_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
