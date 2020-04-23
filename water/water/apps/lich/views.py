import tkinter as tk
from tkinter import filedialog

from django.shortcuts import render

from .models import Menu_item, Kotel, Lich
from .imports import LichImport

menu_list = Menu_item.objects.all().order_by('parent_id', 'menu_id')

def index(request):
    return render(request, 'index.html', {'main_menu': menu_list})


def imp_lich(request):
    root = tk.Tk()
    root.withdraw()
    txt_ = filedialog.askopenfilename()

    file_ = open(txt_, 'r')
    lines = file_.readlines()
    for line in lines:
        new_import = LichImport(line)
        new_import.lich_add()   
    file_.close()

    #one_lich_ = Lich.objects.get(kod=lich_id)
    one_lich_ = lines
    return render(request, 'lichs.html', {'main_menu': menu_list, 'lichs': one_lich_})


def kotels(request):
    kotels_ = Kotel.objects.all().order_by('kot_kod')
    return render(request, 'kotels.html', {'main_menu': menu_list, 'kotels': kotels_})

def lichs(request):
    lichs_ = Lich.objects.all().order_by('kod')
    return render(request, 'lichs.html', {'main_menu': menu_list, 'lichs': lichs_})
