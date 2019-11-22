from review import Review
import unittest
import random

class TestReview(unittest.TestCase):
    """
    Tests for the Review class
    """

    def test_init_none_text(self):
        text = None
        self.assertRaises(TypeError, Review.__init__,text)

    def test_get_text(self):
        r = Review("Sample text.")
        actual = r.get_text()
        expected = "Sample text."
        self.assertEqual(actual, expected)

    def test_set_positivity_float(self):
        r = Review("Test review.")
        for _ in range(1000):
            random_number = random.random()
            r.set_positivity(random_number)
            self.assertEqual(r.positivity, random_number)
    
    def test_set_positivity_int(self):
        r = Review("Testing review.")
        for _ in range(1000):
            random_number = random.randint(0,10)
            r.set_positivity(random_number)
            self.assertEqual(r.positivity, random_number)

    def test_to_string(self):
        r = Review("Testing review.")
        for _ in range(1000):
            rand_num = random.random()
            r.set_positivity(rand_num)
            expected = "<--- Review Text ---> \n" + r.get_text() + "\n <--- Positivity ---> \n"+str(r.positivity)+"\n"
            actual = r.__str__()
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()    