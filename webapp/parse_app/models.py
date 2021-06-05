from django.db import models
import datetime
from django.conf import settings

class Source (models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    link = models.CharField(null=False, max_length=200)

class Place (models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    link = models.CharField(null=False, max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Parameters (models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    value = models.CharField(null=False, max_length=1000)
    def __str__(self):
        return self.name

class StopWords (models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Review (models.Model):
    class Meta:
        unique_together = (('source', 'source_id'),)

    text = models.CharField(max_length=3000)
    date_create = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    review_date = models.DateTimeField()
    source_inner_id = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    stars = models.IntegerField()
    translated = models.BooleanField()
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

    def __str__(self):
        return self.source+": "+self.source_inner_id
