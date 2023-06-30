#!/usr/bin/python3
import unittest


def suma(a, b):
    if type(a) is not int:
        raise TypeError("a")
    if type(b) is not int:
        raise TypeError("b")
    return a + b


class test_suma(unittest.TestCase):
    "comentario"

    def test_suma_comun(self):
        self.assertEqual(suma(1, 2), 3)

    def test_type(self):
        with self.assertRaises(ValueError):
            suma("hola", 2)
