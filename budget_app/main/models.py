from django.db import models
from django.db.models import Sum
# Create your models here.


class Income(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

    @classmethod
    def total_user_spend(cls):
        return cls.objects.aggregate(total=Sum('amount'))

    def __str__(self):
        return self.title


class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

    @classmethod
    def total_user_spend(cls):
        return cls.objects.aggregate(total=Sum('amount'))

    def __str__(self):
        return self.title
