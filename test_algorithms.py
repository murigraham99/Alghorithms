import unittest
import algorithms


class TestAlgorithms(unittest.TestCase):
    def test_max(self):
        self.assertEqual(algorithms.max(1, 2, 3), 3)
        self.assertEqual(algorithms.max(0, 0, 0), 0)
        self.assertEqual(algorithms.max(-1, -2, -3), -1)
        with self.assertRaises(ValueError):
            algorithms.max(1, -1, -99999999)

    def test_prime(self):
        self.assertEqual(algorithms.prime(7), "prime")
        self.assertEqual(algorithms.prime(4), "not prime")
        with self.assertRaises(ValueError):
            algorithms.prime(-2)

    def test_fibonacci(self):
        self.assertEqual(algorithms.fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(algorithms.fibonacci(0), 0)
        self.assertEqual(algorithms.fibonacci(1), [0, 1])
        self.assertEqual(len(algorithms.fibonacci(9999)), 9999)

    def test_max_list(self):
        self.assertEqual(algorithms.max_list([1, 2, 3]), 3)
        self.assertEqual(algorithms.max_list([0, 0, 0]), 0)
        self.assertEqual(algorithms.max_list([-1, -2, -3]), -1)
        with self.assertRaises(ValueError):
            algorithms.max_list([1, -1, -99999999])

    def test_min(self):
        self.assertEqual(algorithms.min_list([1, 2, 3]), 1)
        self.assertEqual(algorithms.min_list([0, 0, 0]), 0)
        self.assertEqual(algorithms.min_list([-1, -2, -3]), -3)
        with self.assertRaises(ValueError):
            algorithms.min_list([1, -1, 999999999999])

    def test_sum_digits(self):
        self.assertEqual(algorithms.sum_digits(123), 6)
        self.assertEqual(algorithms.sum_digits(-111), -3)

    def test_palindrome(self):
        self.assertEqual(algorithms.palindrome(101), "palindrome")
        self.assertEqual(algorithms.palindrome(102), "not palindrome")
        self.assertEqual(algorithms.palindrome(1), "palindrome")

    def test_sum_last_digit(self):
        self.assertEqual(algorithms.sum_last_digit(1234), 6)
        self.assertEqual(algorithms.sum_last_digit(1), 0)


if __name__ == '__main__':
    unittest.main()
