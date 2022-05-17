from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from carear.models import Carear,CarearChecker,TravelIncome,IncreaseIncome,DecreaseIncome,DailyIncome,WeeklyIncome
from carear.serializers import CarearSerializer, UserSerializer, CarearCheckerSerializer,TravelIncomeSerializer,WeeklyIncomeSerializer,DailyIncomeSerializer,IncreaseIncomeSerializer,DecreaseIncomeSerializer


class CarearViewSet(viewsets.ModelViewSet):
    queryset = Carear.objects.all()
    serializer_class = CarearSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']
    permission_classes = (permissions.IsAuthenticated,)


class CarearCheckerViewSet(viewsets.ModelViewSet):
    queryset = CarearChecker.objects.all()
    serializer_class = CarearCheckerSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']

    # overwriting creat permission for Author
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAdminUser, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]
        return super(self.__class__, self).get_permissions()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # overwriting creat permission for usercreation
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAdminUser, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]
        return super(self.__class__, self).get_permissions()

class TravelIncomeViewSet(viewsets.ModelViewSet):
    queryset = TravelIncome.objects.all()
    serializer_class = TravelIncomeSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']

class IncreaseIncomeViewSet(viewsets.ModelViewSet):
    queryset = IncreaseIncome.objects.all()
    serializer_class = IncreaseIncomeSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']


class DecreaseIncomeViewSet(viewsets.ModelViewSet):
    queryset = DecreaseIncome.objects.all()
    serializer_class = DecreaseIncomeSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']

class DailyIncomeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    @action(detail=True, methods=['get'])
    def get_sum_daily(self, request):
        user = self.get_object()
        travel_income=TravelIncome.objects.filter(carear=user)
        increase_income=IncreaseIncome.objects.all(carear=user)
        decrease_income=DecreaseIncome.objects.all(carear=user)
        sum_income = travel_income+decrease_income+increase_income
        serializer = DailyIncomeSerializer(date=datetime.now(),sum_amount=sum_income,carear=user)
        if serializer.is_valid():
            serializer.save()
            serializer.create(serializer)
            return Response({'status': 'dailyincome updated'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class WeeklyIncomeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get','create']
    @action(detail=True, methods=['get'])
    def get_sum_weekly(self, request):
        from_date= request.data['from_date']
        to_date= request.data['to_date']
        user = self.get_object()
        if isinstance(user, CarearChecker):

            travel_income = DailyIncome.objects.filter(carear=user,date__range=[from_date, to_date])
            sum_weekly_amount=0
            for travel in travel_income:
                amount = travel['amount']
                sum_weekly_amount+=amount
            serializer = WeeklyIncomeSerializer(date=datetime.now(), sum_amount=sum_weekly_amount, carear=user)
            if serializer.is_valid():
                serializer.save()
                serializer.create(serializer)
                return Response({'status': 'weeklyincome updated'})
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

    # TODO permission only for checker users
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        # elif self.action in ['create']:
        #     self.permission_classes = [permissions.IsAdminUser, ]
        # else:
        #     self.permission_classes = [permissions.AllowAny, ]
        # return super(self.__class__, self).get_permissions()