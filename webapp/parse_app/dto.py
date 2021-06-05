import datetime

class ReviewDTO:
    def __init__(self, text : str, review_date : str, source : str, review_id : str, place : str):
        self.text = text
        self.review_date = review_date
        self. source = source
        self.review_id = review_id
        self.place = place
