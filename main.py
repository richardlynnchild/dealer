# This script will scrape reviews from a car dealership review
# website. It will build an array of Reviews, assign each
# Review a posivity rating, then sort the array by this
# positivity rating. The top three "most positive"
# reviews will be logged to the console.
#
# Author: Richard Child
# Last updated: November 21, 2019

import scraper
from positivity_calculator import PositivityCalculator

pcalc = PositivityCalculator('positive-words.txt')
review_texts = scraper.scrape(1,5)
reviews = scraper.process_reviews(review_texts, pcalc)
scraper.print_top_three_reviews(reviews)


