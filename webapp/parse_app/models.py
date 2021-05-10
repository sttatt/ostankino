from django.db import models
import datetime

class Review (models.Model):
    text = models.CharField(max_length=3000)
    date_create = models.DateField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    review_date = models.DateField()
    source = models.CharField(max_length=200)
    review_id = models.IntegerField()
    place = models.CharField(max_length=200)