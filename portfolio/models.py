from django.db import models
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PortfolioModel(models.Model):
    title = models.CharField(max_length=155)
    link = models.CharField(max_length=155)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_location, blank=True, null=True)
    publish_date = models.DateField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class AnyProblemsModel(models.Model):
    title = models.CharField(max_length=155)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)


class ContactUsModel(models.Model):
    full_name = models.CharField(max_length=155)
    number = models.CharField(max_length=155)

    def __str__(self):
        return str(self.full_name)


class AskedQuestionsModel(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return str(self.question)


class OurTeamModel(models.Model):
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class OurPartnersModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return str(self.title)


class PartnersLogoModel(models.Model):
    image = models.ImageField(upload_to=upload_location)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.id)




