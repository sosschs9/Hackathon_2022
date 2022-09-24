from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('reser/', views.new),
    path('reser/normal/', views.normalmove),
    path('reser/unnormal/', views.unnormalmove),
    path('out/', views.outs),
    path('join/', views.joins),
    path('help/', views.helps),
    path('login/', views.logins),
    path('see/', views.sees),
    path('reser/normal/normal_list/search/', views.searches),
    path('reser/normal/normal_list/search/bus_watch', views.watches),
    path('reser/normal/normal_list/search/bus_watch/bus_reser', views.reservation),
    path('reser/normal/normal_list/search/bus_watch/bus_reser/check', views.finalcheck),
    path('reser/normal/normal_list/search/bus_watch/bus_reser/check/reser_list', views.reserlist),
    path('reser/normal/normal_list', views.normallist),
    path('reser/unnormal/unnormal_list', views.unnormallist),
    path('reser/unnormal/unnormal_list/unnormal_search', views.unnormalsearch),
    path('reser/unnormal/unnormal_list/unnormal_search/unnormal_watch', views.unnormalwatch),
    path('reser/unnormal/unnormal_list/unnormal_search/unnormal_watch/unnormal_check', views.unnormalcheck),
]