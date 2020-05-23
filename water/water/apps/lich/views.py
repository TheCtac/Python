from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from .models import Menu_item, Kotel, Lich, Boiler, Typel, Diln
from .controlers.imports import ModelImport
from .controlers.consumption import Consumption

menu_list = Menu_item.objects.all().order_by('parent_id', 'menu_id')

def index(request):
    return render(request, 'index.html', {'main_menu': menu_list})


def imp_water(request):

    #return HttpResponse("Ahtung!")
    new_import = ModelImport()
    new_import.lich_add()
    new_import.close()
    
    boilers_ = get_list_or_404(Boiler)
    return render(request, 'kotels.html', {'main_menu': menu_list, 'kotels': boilers_})


def kotels(request):
    kotels_ = Kotel.objects.all().order_by('kot_kod')
    return render(request, 'kotels.html', {'main_menu': menu_list, 'kotels': kotels_})

def boilers(request):
    boilers_ = get_list_or_404(Boiler)
    return render(request, 'kotels.html', {'main_menu': menu_list, 'kotels': boilers_})

def lichs(request):
    lichs_ = Lich.objects.all().order_by('kod')
    return render(request, 'lichs.html', {'main_menu': menu_list, 'lichs': lichs_})

def lich_type(request):
    types_ = Typel.objects.all()
    return render(request, 'lichs.html', {'main_menu': menu_list, 'lichs': types_})

def diln(request):
    types_ = Diln.objects.all()
    return render(request, 'lichs.html', {'main_menu': menu_list, 'lichs': types_})

def counter_val(request):
    consum = Consumption()
    counter_vals = consum.get_counter_val()
    return render(request, 'counter_val.html', {'main_menu': menu_list, 'counter_vals': counter_vals})

