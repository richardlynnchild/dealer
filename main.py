# This script will scrape reviews from a car dealership review
# website. It will build an array of Reviews, assign each
# Review a posivity rating, then sort the array by this
# positivity rating. The top three "most positive"
# reviews will be logged to the console.
#
# Author: Richard Child
# Last updated: November 21, 2019

from bs4 import BeautifulSoup
from review import Review
from positivity_calculator import PositivityCalculator
import requests

pcalc = PositivityCalculator('positive-words.txt')

PAGE_START = 1
PAGE_END = 5
reviews = []

# Scrape the data from pages 1-5
for page in range(PAGE_START, PAGE_END + 1):

    print("Scraping page"+str(page)+"...")
    url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page"+str(page)+"/?filter=ALL_REVIEWS#link"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    # Get the reviews on this page
    for p in soup.select("p.review-content"):

        # Make a Review object and calculate
        # its positivity rating using the
        # PositivityCalculator object
        rev = Review(p.get_text())
        pos = pcalc.calc_positivity(rev.get_text())
        rev.set_positivity(pos)

        # Add to the reviews array
        reviews.append(rev)

# Sort array by Positivity Rating
reviews.sort(key= lambda x: x.positivity, reverse=True)

# Log top three to console
print("Here are the top three MOST POSITIVE REVIEWS .....")
print(reviews[0])
print(reviews[1])
print(reviews[2])

