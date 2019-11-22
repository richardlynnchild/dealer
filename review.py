class Review:
    """
    Review represents an online review
    It contains the text of the review as well
    as the positivity rating. This value
    attempts to capture how positive the review is.
    """
    def __init__(self, text):
        """
        Constructor that assigns review text

        Parameters:
            text: the review text
        """
        if text is None:
            raise TypeError("Expected string but received NoneType")
        self.text = text

    def get_text(self):
        """
        Get the review text

        Returns:
            text: the review text
        """
        return self.text

    def set_positivity(self, rating):
        """
        Set the positivity rating for the review

        Parameters:
            rating: the rating for this review
        """
        self.positivity = rating

    def __str__(self):
        """
        Returns:
            toString: a string describing this review
        """
        toString = "<--- Review Text ---> \n"
        toString += self.text
        toString += "\n <--- Positivity ---> \n" + str(self.positivity) + "\n"
        return toString