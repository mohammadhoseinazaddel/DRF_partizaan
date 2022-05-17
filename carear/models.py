from django.db import models
from django.contrib.auth.models import User

class Carear(models.Model):
    carear_name = models.CharField(max_length=20, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    def __str__(self):
        return self.carear_name

class CarearChecker(models.Model):
    checker_name = models.CharField(max_length=20, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    def __str__(self):
        return self.checker_name

class TravelIncome(models.Model):
    carear = models.ManyToOneRel(Carear, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()

class IncreaseIncome(models.Model):
    carear = models.ManyToOneRel(Carear, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()

class DecreaseIncome(models.Model):
    carear = models.ManyToOneRel(Carear, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()

class DailyIncome(models.Model):
    carear = models.ManyToOneRel(Carear, on_delete=models.CASCADE)
    date = models.DateField()
    sum_amount = models.IntegerField()

class WeeklyIncome(models.Model):
    carear = models.ManyToOneRel(Carear, on_delete=models.CASCADE)
    date = models.DateField()
    sum_amount = models.IntegerField()