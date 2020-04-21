from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('huy', views.huy, name='huy'),
    path('<int:lich_id>', views.one_lich, name='one_lich'),
    path('kotels', views.kotels, name='kotels'),
    path('lichs', views.lichs, name='lichs'),    
]