from review import Review
from positivity_calculator import PositivityCalculator
import scraper
import unittest

class TestScraper(unittest.TestCase):

    """
    Tests for the functions in scraper 
    """
    
    def test_scrape(self):
        texts = scraper.scrape(1,1,logging=False)
        actual = len(texts)
        expected = 10
        self.assertEqual(actual, expected)

    def test_process_reviews(self):
        pc = PositivityCalculator('positive-words.txt')
        texts = ["Test01 review.", "Test02 review.", "Test03 review."]
        reviews = scraper.process_reviews(texts, pc)
        self.assertEqual(len(reviews), 3)
        for i in range(len(texts)-1):
            self.assertTrue(reviews[i].get_text() == texts[i])
            self.assertTrue(reviews[i].positivity is not None)

        

if __name__ == '__main__':
    unittest.main() 