from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
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
    queryset = DailyIncome.objects.all()
    serializer_class = DailyIncomeSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']

class WeeklyIncomeViewSet(viewsets.ModelViewSet):
    queryset = WeeklyIncome.objects.all()
    serializer_class = WeeklyIncomeSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']

    # TODO permission only for checker users
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        # elif self.action in ['create']:
        #     self.permission_classes = [permissions.IsAdminUser, ]
        # else:
        #     self.permission_classes = [permissions.AllowAny, ]
        # return super(self.__class__, self).get_permissions()