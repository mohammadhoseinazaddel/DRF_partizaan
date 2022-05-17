

from django.views.generic.list import ListView
from carear.models import WeeklyIncome
class WeeklyShow(ListView):
    model = WeeklyIncome
    template_name = 'weekly.html'

    def get_queryset(self):
        from_date = self.request.GET.get('fromdate')
        to_date = self.request.GET.get('todate')
        self.queryset = WeeklyIncome.objects.all()
        if from_date:
            self.queryset.filter(from_date__gte=from_date)
        if to_date:
            self.queryset.filter(to_date__lte=to_date)
        return self.queryset