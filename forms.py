
from django import forms
from django.shortcuts import render


class WeekForm(forms.Form):
    from_date = forms.DateField()
    to_date = forms.DateField()

def history(request):
    if request.method == "POST":
        week_form = WeekForm(request.POST)
        if week_form.is_valid():
           form = week_form.save(commit=False)
           form.save()
           return ('results')
    else:
       week_form = WeekForm()

    return render(request, 'carear/templates/weekly.html', {'week_form': week_form})