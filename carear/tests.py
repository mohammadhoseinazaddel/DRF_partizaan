from django.test import TestCase
from .models import *
import datetime

# modeltest
class CarearTest(TestCase):
    def setUp(self):
        Carear.objects.create(
            carear_name='test',user='test')

class TravelIncomeTest(TestCase):
    def setUp(self):
        TravelIncome.objects.create(
            carear='test',date=datetime.date(2010, 1, 2),amount=240)

class IncreaseIncomeTest(TestCase):
    def setUp(self):
        IncreaseIncome.objects.create(
            carear='test',date=datetime.date(2010, 1, 2),amount=240)

class DecreaseIncomeTest(TestCase):
    def setUp(self):
        DecreaseIncome.objects.create(
            carear='test',date=datetime.date(2010, 1, 2),amount=240)

class DailyIncomeTest(TestCase):
    def setUp(self):
        DailyIncome.objects.create(
            carear='test',date=datetime.date(2010, 1, 2),sum_amount=240)

class CarearCheckerTest(TestCase):
    def setUp(self):
        CarearChecker.objects.create(
            checker_name='test',user='test')

# ToDo daily api test

