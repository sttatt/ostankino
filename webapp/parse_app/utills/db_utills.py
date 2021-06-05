from ..models import Review, Parameters
from ..dto import ReviewDTO

def save_reviews(review : ReviewDTO):
    review = Review(text=review.text,
                    review_date=review.review_date,
                    source=review.source,
                    review_id=review.review_id,
                    place=review.place)
    review.save()

def get_parameter_value(name):
    parameter = Parameters.objects.get(name=name)
    print(123)
    return parameter.value