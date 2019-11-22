class PositivityCalculator:
    """
    PositivityCalculator will calculate a positivity rating
    for a string of text. A text file of positive words is
    used to construct the calculator. Then it can perform
    the calculation when calc_positivity is called.
    """
    def __init__(self, path):
        """
        Read in a text file with positive words

        Parameters:
            path: the file path the positive words text file
        """

        with open(path,'r') as reader:
            self.positive_words = [line.rstrip() for line in reader]

    def calc_positivity(self, text):
        """
        Calculate the positivity rating for this string of text.
        Positivity rating is defined as number of positive words
        divided by total number of words in text. Positive words
        have been loaded when object was constructed.

        Parameters:
            text: the string to calculate rating for

        Returns:
            positivity: the rating
        """

        num_nice_words = 0
        words = text.split(' ')
        for word in words:
            if self.positive_words.count(word):
                num_nice_words += 1
        positivity = num_nice_words / len(words)
        return positivity
