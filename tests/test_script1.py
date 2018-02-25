from unittest import TestCase
from my_python_learning_scripts.script1 import parse_file, get_numbers


class TestScript1(TestCase):
    """
    pass
    """

    def test_get_numbers(self):
        """
        Function should receive a list  and return only the numbers that are present in that list,  even if the
        numbers are string.
        :return:
        """
        self.assertEqual([1, 2, 3], get_numbers(["1", "2", "3"]))

    def test_get_numbers_intercalated(self):
        self.assertEqual([1, 2, 3], get_numbers(["1", "abc", "2", "abc2", "3"]))

    def test_get_numbers_none(self):
        self.assertEqual([], get_numbers(["abc", "abc2"]))

    def test_get_numbers_ints(self):
        self.assertEqual([1, 2, 3], get_numbers(["abc", "abc2", 1, 2, 3]))

    def test_get_numbers_floats(self):
        self.assertEqual([1.0, 2.0, 3], get_numbers(["abc", "1.0", "abc2", 2.0, 3]))


class Test_Files(TestCase):
    def assert_whatever(self, input, expected):
        z = open("input.txt", "w")
        for i in input:
            z.write(str(i))
            z.write("\n")
        z.close()
        parse_file("input.txt")
        o = []
        with open("out.txt", "r") as l:
            for line in l:
                o.append(line.rstrip("\n"))
        self.assertEqual(expected, o)

    def test_get_numbers(self):
        self.assert_whatever(["1", "2", "3"], ["1", "2", "3"])

    def test_get_numbers_intercalated(self):
        self.assert_whatever(["1", "abc", "2", "abc2", "3"], ["1", "2", "3"])

    def test_get_numbers_none(self):
        self.assert_whatever(["abc", "abc2"], [])

    def test_get_numbers_ints(self):
        self.assert_whatever(["abc", "abc2", 1, 2, 3], ["1", "2", "3"])

    def test_get_numbers_floats(self):
        self.assert_whatever(["abc", "1.0", "abc2", 2.0, 3], ["1.0", "2.0", "3"])
