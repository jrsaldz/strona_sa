from django.db import models

# Create your models here.


class DzienTygodnia(models.Model):
    nazwa = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15)


class Miasto(models.Model):
    nazwa = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)


class Mityng(models.Model):
    nr_telefonu = models.CharField(max_length=20, blank=False)
    pin = models.CharField(max_length=10, blank=True)
    godzina = models.PositiveSmallIntegerField()
    minuta = models.PositiveSmallIntegerField()
    dzien_tygodnia = models.ForeignKey(DzienTygodnia, on_delete=models.CASCADE)
    miasto = models.ForeignKey(Miasto, on_delete=models.CASCADE)
