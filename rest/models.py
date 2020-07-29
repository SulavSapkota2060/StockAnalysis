from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=400,null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Stocks(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Just(models.Model):
    symbol = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)


    def __str__(self):
        return self.symbol


class UpStat(models.Model):
    stat = models.BooleanField(default=False)