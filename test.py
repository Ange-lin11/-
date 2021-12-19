import unittest
import main
import time

class TestCalculator(unittest.TestCase):
    def test_add(self):
        input = 'input.txt'
        main.write_file(input, [1, 2, 3, 4])
        self.assertEqual(main.sum_array(input), 10)

        main.write_file(input, [100, -100, 88, -88, 0])
        self.assertEqual(main.sum_array(input), 0)

        main.write_file(input, [-100, 10, 100 ** 12, 40])
        self.assertEqual(main.sum_array(input), -100 + 10 + 100 ** 12 + 40)

    def test_mult(self):

        input = 'input.txt'

        main.write_file(input, [1, 2, 3, 4])
        self.assertEqual(main.mult_array(input), 24)

        main.write_file(input, [12, 10000, 888, 3753 ** 3757, 0])
        self.assertEqual(main.mult_array(input), 0)

        main.write_file(input, [1000 ** 10, 100 ** 100, 1000 ** 6, 10])
        self.assertEqual(main.mult_array(input),  1000 ** 10 * 100 ** 100 * 1000 ** 100 * 10)

    def test_min(self):

        input = 'input.txt'

        main.write_file(input, [1, 2, 3, 4])
        self.assertEqual(main.min_array(input), 1)

        main.write_file(input, [-50, 100 ** 10, 300, -80000, -100 ** 100])
        self.assertEqual(main.min_array(input), -100 ** 100)

        main.write_file(input, [10, 100, 90, 0, 98, 1000 ** 10])
        self.assertEqual(main.min_array(input), 0)

    def test_max(self):

        input = 'input.txt'

        main.write_file(input, [1, 2, 3, 4])
        self.assertEqual(main.max_array(input), 4)

        main.write_file(input, [-50, 100 ** 10, 300, -80000, -100 ** 100])
        self.assertEqual(main.max_array(input), 100 ** 10)

        main.write_file(input, [-3000, -100, -299, 0, -100 ** 10])
        self.assertEqual(main.max_array(input), 0)

    def test_sum_min_max(self):

        input = 'input.txt'

        main.write_file(input, [1, 2, 3, 4])
        self.assertEqual(main.sum_min_max_array(input), 5)

        main.write_file(input, [-1, 100, 99, 15, -99, -100])
        self.assertEqual(main.sum_min_max_array(input), 0)

        main.write_file(input, [-100 ** 10, 0, 100 ** 100, 1])
        self.assertEqual(main.sum_min_max_array(input), -100 ** 10 + 100 ** 100)

    def test_time(self):
        input = 'input.txt'
        begin = time.time()

        main.write_file(input, [1, 2, 3, 4, 5])
        main.sum_array(input)
        main.mult_array(input)
        main.min_array(input)
        main.max_array(input)
        main.sum_min_max_array(input)
        self.assertLess(time.time() - begin, 1.5)

        main.write_file(input, [i for i in range(100)])
        main.sum_array(input)
        main.mult_array(input)
        main.min_array(input)
        main.max_array(input)
        main.sum_min_max_array(input)
        self.assertLess(time.time() - begin, 1.5)


if __name__ == "__main__":
    unittest.main()
print()
