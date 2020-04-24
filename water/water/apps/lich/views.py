from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu_item, Kotel, Lich
from .imports import ModelImport

menu_list = Menu_item.objects.all().order_by('parent_id', 'menu_id')

def index(request):
    return render(request, 'index.html', {'main_menu': menu_list})


def imp_water(request):

    return HttpResponse("Ahtung!")
    new_import = ModelImport()
    new_import.kotel_add()
    new_import.close()
    
    kotels_ = Kotel.objects.all().order_by('kot_kod')
    return render(request, 'kotels.html', {'main_menu': menu_list, 'kotels': kotels_})


def kotels(request):
    kotels_ = Kotel.objects.all().order_by('kot_kod')
    return render(request, 'kotels.html', {'main_menu': menu_list, 'kotels': kotels_})


def lichs(request):
    lichs_ = Lich.objects.all().order_by('kod')
    return render(request, 'lichs.html', {'main_menu': menu_list, 'lichs': lichs_})
