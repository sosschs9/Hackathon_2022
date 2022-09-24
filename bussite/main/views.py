#달려라달구벌 main페이지 / views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main.html')

def new(request):
    return render(request, 'reser.html')

def normalmove(request):
    return render(request, 'normal.html')

def unnormalmove(request):
    return render(request, 'unnormal.html')

def helps(request):
    return render(request, 'help.html')

def joins(request):
    return render(request, 'join.html')

def outs(request):
    return render(request, 'out.html')

def logins(request):
    return render(request, 'login.html')

def sees(request):
    return render(request, 'see.html')

def searches(request):
    return render(request, 'search.html')

def watches(request):
    return render(request, 'bus_watch.html')

def reservation(request):
    return render(request, 'bus_reser.html')

def finalcheck(request):
    return render(request, 'check.html')

def reserlist(request):
    return render(request, 'reser_list.html')

def normallist(request):
    return render(request, 'normal_list.html')

def unnormallist(request):
    return render(request, 'unnormal_list.html')

def unnormalsearch(request):
    return render(request, 'unnormal_search.html')

def unnormalwatch(request):
    return render(request, 'unnormal_watch.html')

def unnormalcheck(request):
    return render(request, 'unnormal_check.html')

#class FormView(generic.View):
 #   template_name = 'templates/test.html'
  #  result = keyword.keywordFindAPI(inputkw)
   # context = {
    #    'result' : result
    #}
    #return render(request, self.template_name, context)