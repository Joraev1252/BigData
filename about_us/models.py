from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.


class OurCoursesModel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return str(self.title)


class AboutUsModel(models.Model):
    body = models.TextField()
    phone_number = models.IntegerField()
    social_media_link = models.CharField(max_length=155)

    def __str__(self):
        return str(self.body)


class OurGeneralStatisticsModel(models.Model):
    title = models.CharField(max_length=355)
    number = models.CharField(max_length=55)

    def __str__(self):
        return str(self.title)
