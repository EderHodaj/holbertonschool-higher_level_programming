#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys
import json


class TestSquare(unittest.TestCase):
    """class TestSquare"""
    def test_id(self):
        """check instance was created"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertIsNotNone(id(s1))

    def test_init(self):
        """check that instance was created from correct class"""
        Base._Base__nb_objects = 0
        s2 = Square(5)
        self.assertIsInstance(s2, Square)
        self.assertTrue(issubclass(type(s2), Rectangle))

    def test_invalid_y_type(self):
        """Test that creating a Square with a non-integer y raises a TypeError."""
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    def test_invalid_size_type(self):
        """Test that creating a Square with a non-integer size raises a TypeError."""
        with self.assertRaises(TypeError):
            s = Square(1, "2")
        
    def test_numObj(self):
        """check number of instances created"""
        Base._Base__nb_objects = 0
        s3 = Square(2, 2)
        s4 = Square(5, 5)
        self.assertEqual(s4.id, 2)

    def test_zero_size(self):
        """check zero size"""
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_x(self):
        """check negative x"""
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -3)

    def test_negative_size(self):
        """check negative size"""
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_negative_y(self):
        """check negative y"""
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 3, -1)

    def test_one_string(self):
        """check one string"""
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_getterAndSetter(self):
        """check getter and setter"""
        Base._Base__nb_objects = 0
        s5 = Square(5)
        self.assertEqual(s5.width, 5)
        self.assertEqual(s5.height, 5)
        s5 = Square(2, 2)
        self.assertEqual(s5.width, 2)
        self.assertEqual(s5.height, 2)
        self.assertEqual(s5.x, 2)
        s5 = Square(3, 1, 3)
        self.assertEqual(s5.width, 3)
        self.assertEqual(s5.height, 3)
        self.assertEqual(s5.x, 1)
        self.assertEqual(s5.y, 3)

    def test_area(self):
        """check area"""
        Base._Base__nb_objects = 0
        s6 = Square(5)
        self.assertEqual(s6.area(), s6.width * s6.height)

    def test_save_to_file(self):
        """Check save_to_file method"""
        Base._Base__nb_objects = 0
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]", "Failed to save empty list")
        s1 = Square(5)
        s2 = Square(2, 2)
        Square.save_to_file([s1, s2])
        list_input = [s1.to_dictionary(), s2.to_dictionary()]
        with open("Square.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertTrue(list_input == list_dict, "Failed to save list of Square objects")

    def test_save_to_file_None(self):
        """check save_to_file with None"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertTrue(list_dict == [])

    def test_display(self):
        """check display"""
        Base._Base__nb_objects = 0
        s7 = Square(5)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "#####\n#####\n#####\n#####\n#####\n")
        s8 = Square(2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s8.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "  ##\n  ##\n")
        s9 = Square(3, 1, 3)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s9.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n\n ###\n ###\n ###\n")

    def test_str(self):
        """check str"""
        Base._Base__nb_objects = 0
        s8 = Square(5)
        s9 = Square(2, 2)
        s10 = Square(3, 1, 3)
        string1 = s8.__str__()
        string2 = s9.__str__()
        string3 = s10.__str__()
        self.assertEqual(string1, "[Square] ({:d}) 0/0 - 5".format(s8.id))
        self.assertEqual(string2, "[Square] ({:d}) 2/0 - 2".format(s9.id))
        self.assertEqual(string3, "[Square] ({:d}) 1/3 - 3".format(s10.id))

    def test_display_xy(self):
        """check display with xy attributes"""
        Base._Base__nb_objects = 0
        s1 = Square(2, 3, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n   ##\n   ##\n")
        s2 = Square(3, 2, 1)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s2.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n  ###\n  ###\n  ###\n")

    def test_dictionary(self):
        """check dictionary conversion"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1, 1)
        a_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1_dictionary = s1.to_dictionary()
        self.assertTrue(s1_dictionary == a_dict)
