from django.db import models

# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=100)
    bpub_date = models.DateField()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)