#from djongo import models
from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    unrealizedGains = models.FloatField(null=True, editable=False, blank=True)
    realizedGains = models.FloatField(null=True, default=0.0, editable=False, blank=True)
    expRet = models.FloatField(null=True, editable=False, blank=True)
    beta = models.FloatField(null=True, editable=False, blank=True)


class Stock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True, default=0)
    buyRate = models.FloatField(null=True, default=0.00)
    buyDate = models.DateField(null=True, blank=True, default="")
    sellRate= models.FloatField(null=True, default=0.00)
    sellDate = models.DateField(null=True, blank=True, default="")
    unrealizedGains = models.FloatField(null=True, default=0.00, editable=False)
    realizedGains = models.FloatField(null=True, default=0.00, editable=False)
    target = models.FloatField(null=True, default=0.00)
    beta = models.FloatField(null=True, default=0.00, editable=False)


def __str__(self):
    return self.name