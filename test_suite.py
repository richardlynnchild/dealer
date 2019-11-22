"""
The test suite for all the classes in the Dealer project
"""

import unittest
import test_review
import test_scraper
import test_positivity_calculator

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_review))
suite.addTests(loader.loadTestsFromModule(test_scraper))
suite.addTests(loader.loadTestsFromModule(test_positivity_calculator))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)

if __name__ == '__main__':
    unittest.main() 