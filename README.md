# A Dealer for the People
The goal for this project is to determine the most positive reviews listed
for the car dealership *McKaig Chevrolet Buick* on the website **dealerrater.com**.
The script `main.py` will perform the web scraping on the first five pages of
reviews on the website. Some console output will appear to indicate the progress
of the web scraping.

The positivity rating will then be calculated for each review. The top three
"most positive" reviews will be logged to the console.

## How to run
To run this script use `python3 main.py`
To install all required python packages use `pip3 install -r requirements.txt`

## Positivity Ratings
Positivity rating is defined as the number of positive words in a review divided by the total
number of words in the review. For example, if a review contains 20 positive words
and is 80 words long, then the positivity rating would be **0.25**.

A text file of "positive" words has been included in this project. It was taken
from https://gist.github.com/mkulakowski2/4289437 and is the result of the following
studies:

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
      Proceedings of the ACM SIGKDD International Conference on Knowledge 
      Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
      Washington, USA
      
Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
      and Comparing Opinions on the Web." Proceedings of the 14th 
      International World Wide Web conference (WWW-2005), May 10-14, 
      2005, Chiba, Japan.

see http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html for more information.
