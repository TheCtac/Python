from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kotels', views.kotels, name='kotels'),
    path('boilers', views.boilers, name='boilers'),
    path('diln', views.diln, name='diln'),
    path('lichs', views.lichs, name='lichs'),
    path('lich_type', views.lich_type, name='lich_type'),
    path('water_import', views.imp_water, name='imp_water'),
]