from django.db.models import F
from django.db.models import Q

from lich.models import Lich, Kotel, Boiler, Typel, Diln, Pokaz

class Consumption:
    def __init__(self):
        self.counters_ = Lich.objects.filter(date_open__lte='2020-05-01')
        self.counters_ = self.counters_.filter(Q(date_close=None) | Q(date_close__lte='2020-05-01'))

    def get_counter_val(self):
        vals_ = Pokaz.objects.filter(date__gte='2020-04-01').filter(date__lte='2020-05-01')
        vals_ = vals_.filter(kod_lich__in=self.counters_)
        vals_ = vals_.order_by('kod_lich', 'date')
        return vals_
 