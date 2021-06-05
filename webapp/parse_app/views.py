import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from django.http import HttpResponse
from .dto import ReviewDTO
import datetime
from .utills import db_utills
from . import models
# Create your views here.
def index(request):
    # review = ReviewDTO(text="123", review_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
    #                    source = 'google',
    #                    review_id = 'agkd;s123gk123',
    #                    place = 'ostankino'
    #                    )
    # db_utills.save_reviews(review)

    return HttpResponse(db_utills.get_parameter_value('test'))
