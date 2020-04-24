from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kotels', views.kotels, name='kotels'),
    path('lichs', views.lichs, name='lichs'),
    path('water_import', views.imp_water, name='imp_water'),
]