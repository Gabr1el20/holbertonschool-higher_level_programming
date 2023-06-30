#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"Rectangle sub-class unittests"


class Test_init(unittest.TestCase):
    "Test instantiation of Rectangle"

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_only_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_rectangles_id(self):
        rect = Rectangle(8, 4)
        angle = Rectangle(12, 6)
        self.assertEqual(rect.id, angle.id - 1)

    def test_three_args(self):
        rect = Rectangle(8, 4, 0)
        angle = Rectangle(12, 6, 1)
        self.assertEqual(rect.id, angle.id - 1)
