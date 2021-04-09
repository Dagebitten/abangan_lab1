from django.shortcuts import render
from django.http import HttpResponse

from abangan_lab1.forms import NameForm

def home(request):
    if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                UserName = form.cleaned_data["name"]
                return render(request, 'HomePage.html', {'UserName' : UserName})
            else:
                return render(request, 'HomePage.html', {'form' : form})
    else:
        form = NameForm()
    return render(request, 'HomePage.html',  {'form' : form})

def profile(request):
    return render(request, 'ProfilePage.html')

def key(request):
    return render(request, 'KeyPage.html')

def week(request):
    return render(request, 'WeekPage.html')

def today(request):
    return render(request, 'TodayPage.html')


