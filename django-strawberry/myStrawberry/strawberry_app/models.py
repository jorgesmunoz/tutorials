from django.db import models

# Create your models here.


class Fruit(models.Model):
    name = models.CharField(mex_length=20)
    colos = models.ForeignKey(
        'Color', blank=True, null=True, related_name='fruits', on_delete=models.CASCADE)


class Color(models.Model):
    name = models.CharField(max_length=20)
