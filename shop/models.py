from django.db import models


# Create your models here.


class Goods(models.Model):
    g_name = models.CharField(max_length=128)
    g_price = models.IntegerField()


class productionDate(models.Model):
    production_date = models.CharField(max_length=128)
    good = models.ForeignKey('shop.Goods', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
