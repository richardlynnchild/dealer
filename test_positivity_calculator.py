from positivity_calculator import PositivityCalculator
import unittest
import random

class TestPositivityCalculator(unittest.TestCase):
    """
    Tests for the PositivityCalculator class
    """

    def test_positive_words_list_no_newlines(self):
        """
        Make sure the newlines were stripped from the .txt file
        """
        pc = PositivityCalculator('positive-words.txt')
        for word in pc.positive_words:
            newline = '\n'
            self.assertFalse(newline in word)

    def test_positive_word_list_correct_length(self):
        """
        There should be 2006 positive words in the positive-words.txt file
        """
        pc = PositivityCalculator("positive-words.txt")
        self.assertEqual(len(pc.positive_words), 2006)

    def test_zero_positivity(self):
        pc = PositivityCalculator('positive-words.txt')
        negative = "This review is negative and bad and horrible and ugly."
        actual = pc.calc_positivity(negative)
        self.assertEqual(actual, 0.0)

    def test_full_positivity(self):
        pc = PositivityCalculator('positive-words.txt')
        positive = "amazing great astounding awesome good best"
        actual = pc.calc_positivity(positive)
        self.assertEqual(actual, 1.0)

    def test_positivity_ignore_case(self):
        pc = PositivityCalculator('positive-words.txt')
        positive = "Amazing Great Astounding awesome good best"
        actual = pc.calc_positivity(positive)
        self.assertEqual(actual, 1.0)

if __name__ == '__main__':
    unittest.main()    