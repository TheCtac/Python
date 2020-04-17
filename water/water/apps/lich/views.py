from django.shortcuts import render
from django.http import HttpResponse

from .models import Lich, Pokaz, Menu_item


def index(request):
    main_menu = {'main_menu': Menu_item.objects.all().order_by('parent_id', 'menu_id')}
    return render(request, 'index.html', main_menu)


def huy(request):
    return HttpResponse("Hello, huy. You're at the lich/huy.")


def one_lich(request, lich_id):
    return HttpResponse("Hello, huy. You're looking at lich N%s." % lich_id)
