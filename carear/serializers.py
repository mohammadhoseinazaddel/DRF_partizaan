from rest_framework import serializers
from carear.models import TravelIncome, IncreaseIncome, DecreaseIncome, DailyIncome, WeeklyIncome, Carear, CarearChecker
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CarearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carear
        fields = '__all__'

class CarearCheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarearChecker
        fields = '__all__'


class TravelIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelIncome
        fields = '__all__'

    def create(self, validated_data):
        TravelIncome = super().create(validated_data)
        return TravelIncome

class WeeklyIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyIncome
        fields = '__all__'

    def create(self, validated_data):
        Weeklyincome = super().create(validated_data)
        return Weeklyincome

class DailyIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyIncome
        fields = '__all__'

    def create(self, validated_data):
        Dailyincome = super().create(validated_data)
        return Dailyincome

class IncreaseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncreaseIncome
        fields = '__all__'

    def create(self, validated_data):
        Increaseincome = super().create(validated_data)
        return Increaseincome

class DecreaseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecreaseIncome
        fields = '__all__'

    def create(self, validated_data):
        Decreaseincome = super().create(validated_data)
        return Decreaseincome