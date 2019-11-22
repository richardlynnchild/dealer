from bs4 import BeautifulSoup
from review import Review
from positivity_calculator import PositivityCalculator
import requests


def scrape(start, end, logging=True):
    """
    Scrape all the reviews from dealerrater.com for the McKaig 
    Chevrolet Buick dealership.

    Parameters:
        start: the page of reviews to start scraping
        end: the last page of reviews to scrape
    
    Returns:
        texts: a list of strings that are the reviews from the website
    """
    PAGE_START = start
    PAGE_END = end
    texts = []

    # Scrape the data from pages 1-5
    for page in range(PAGE_START, PAGE_END + 1):
        if logging:
            print("Scraping page"+str(page)+"...")
        url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page"+str(page)+"/?filter=ALL_REVIEWS#link"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")

        # Get the reviews on this page
        for p in soup.select("p.review-content"):
            texts.append(p.get_text())
    return texts

def process_reviews(texts, pcalc):
    """
    Take a list of strings, make a list of Review objects and calculate
    the positivity rating for each Review.

    Parameters:
        texts: a list of strings for the Reviews
        pcalc: a PositivityCalculator that will calculate all the ratings
    
    Returns:
        reviews: a list of fully formed Review objects
    """

    reviews = []
    for text in texts:
        rev = Review(text)
        pos = pcalc.calc_positivity(rev.get_text())
        rev.set_positivity(pos)

        # Add to the reviews array
        reviews.append(rev)  
    return reviews

def print_top_three_reviews(reviews):
    """
    Sort array of reviews by positivity rating and print the
    top three to the console

    Parameters:
        reviews: a list of Review objects with positivity ratings
    """
    reviews.sort(key= lambda x: x.positivity, reverse=True)

    # Log top three to console
    print("Here are the top three MOST POSITIVE REVIEWS .....")
    print(reviews[0])
    print(reviews[1])
    print(reviews[2])

