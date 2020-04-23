from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kotels', views.kotels, name='kotels'),
    path('lichs', views.lichs, name='lichs'),
    path('import/lichs', views.imp_lich, name='imp_lich'),
]