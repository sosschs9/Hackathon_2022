from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
import user_info

from .forms import UserForm, BusResrveForm
from .models import ReserveBus, User_db

# Create your views here.
def index(request):
    return render(request, 'reservation/main.html')

def CreatUser(request):
    """
    회원가입
    """
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user_info.add_user(user.username, user.password, user.type)

            return redirect('http://127.0.0.1:8000/reservation')
    else:
        form = UserForm()
    return render(request, 'reservation/join.html', {'form': form})


def BusWatch(request):
    """
    예약 버스 확인
    """
    if request.method == 'POST':
        form = BusResrveForm(request.POST)

        if form.is_valid():
            busname = form.busname
            return render(request, 'reservation/bus_watch.html', busname)
    else:
        form = BusResrveForm()
    return render(request, 'reservation/reserve.html')