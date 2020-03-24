from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unitdetail/<int:number>', views.index, name='unitdetail'),
]
