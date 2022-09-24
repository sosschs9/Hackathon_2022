from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
import user_info

from .forms import UserForm
from .models import User

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
            user_info.add_user(user.name, user.password, user.type)
            return redirect('reservation:login')
    else:
        form = UserForm()
    return render(request, 'reservation/login.html', {'form': form})

