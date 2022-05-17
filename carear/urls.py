from carear import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('carear', views.CarearViewSet)
router.register('CarearCheckerViewSet', views.CarearCheckerViewSet)
router.register('user_creation', views.UserViewSet)
router.register('travelincome', views.TravelIncomeViewSet)
router.register('increaseincome', views.IncreaseIncomeViewSet)
router.register('decreaseincome', views.DecreaseIncomeViewSet)
router.register('dailyincome', views.DailyIncomeViewSet)
router.register('weeklyincome', views.WeeklyIncomeViewSet)

urlpatterns = [

]

urlpatterns += router.urls
