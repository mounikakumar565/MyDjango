from django.db import models

# Create your models here.

# class destination(models.Model):
#
#     Adult = models.IntegerField()
#     Children = models.IntegerField()


class destination(models.Model):

    place = models.TextField()
    city = models.TextField()
    Adult = models.IntegerField()
    Children = models.IntegerField()
    Choose_Your_Destinations = models.TextField()

