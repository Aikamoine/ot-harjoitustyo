import unittest
from someclass import Some_class

class TestSome_class(unittest.TestCase):
    def setUp(self):
        self.testclass = Some_class()

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_method_true(self):
        self.assertTrue(self.testclass.correct())
        
    def test_method_false(self):
        self.assertFalse(self.testclass.incorrect())
        
    def test_attribute(self):
        self.assertEqual(self.testclass.arvo, 10)
