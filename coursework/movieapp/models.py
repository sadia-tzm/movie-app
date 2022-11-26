from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Movie(models.Model):
    '''This is the MOVIE model being used, with fields:
    title, date_released, rating and award_winning.
    '''
    title = models.CharField(max_length=250)
    date_released = models.DateField()
    rating = models.IntegerField(default=0)
    award_winning = models.BooleanField(default=False)

    def __str__(self):
        '''This is a string function that makes the title
        human readable.
        '''
        return self.title

    def to_dict(self):
        '''This function takes a Movie object and returns it
        as a dictionary which makes it easier to read.
        '''
        return {
            'id': self.id,
            'title': self.title,
            'date_released': self.date_released,
            'rating': self.rating,
            'award_winning': self.award_winning,
        }
