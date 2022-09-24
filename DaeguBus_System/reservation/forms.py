from django import forms
from reservation.models import User_db, ReserveBus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User_db
        fields = ['username', 'password', 'type']
        labels = {
            'username': '아이디',
            'password': '비밀번호',
            'type': '사용자 유형',
        }

class BusResrveForm(forms.ModelForm):
    class Meta:
        model = ReserveBus
        fields = ['busname', 'startStation', 'endStation']
        labels = {
            'busname': '버스 이름',
            'startStation': '출발지',
            'endStation': '도착지',
        }
