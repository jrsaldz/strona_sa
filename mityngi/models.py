from django.db import models

# Create your models here.


class DzienTygodnia(models.Model):
    nazwa = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15)

    def __str__(self):
        return self.nazwa


class Miasto(models.Model):
    nazwa = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.nazwa


class Mityng(models.Model):
    nr_telefonu = models.CharField(max_length=20, blank=False)
    pin = models.CharField(max_length=10, blank=True)
    godzina = models.PositiveSmallIntegerField()
    minuta = models.PositiveSmallIntegerField()
    dzien_tygodnia = models.ForeignKey(DzienTygodnia, on_delete=models.CASCADE)
    miasto = models.ForeignKey(Miasto, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} {:02}:{:02}'.format(self.miasto, self.dzien_tygodnia, self.godzina, self.minuta)
