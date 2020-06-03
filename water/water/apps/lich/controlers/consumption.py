from django.db.models import F
from django.db.models import Q

from lich.models import Lich, Kotel, Boiler, Typel, Diln, Pokaz

class Consumption:
    def __init__(self):
        self.counters_ = Lich.objects.filter(date_open__lte='2020-05-01')
        self.counters_ = self.counters_.filter(Q(date_close=None) | Q(date_close__lte='2020-05-01'))
        self.counters_ = self.counters_.order_by('kotel')

    def get_counter_val(self):
        vals_ = Pokaz.objects.filter(date__gte='2020-04-01').filter(date__lte='2020-05-01')
        vals_ = vals_.filter(kod_lich__in=self.counters_)
        vals_ = vals_.order_by('kod_lich', 'date')
        return vals_

    def form_counters(self):
        counter_cons = []
        values = self.get_counter_val()
        for counter in self.counters_:
            counter_con = {
                "kod": counter.kod,
                "number": counter.numb,
                "type": counter.typel,
                "kms": counter.kms,
                "place": counter.place,
                "kotel": counter.kotel,
                "pokaz_b": 0,
                "pokaz_e": 0
            }
            counter_pokaz = values.filter(kod_lich=counter.kod)
            counter_pokaz_len = counter_pokaz.count()
            pokaz_numb = 0
            for pokaz in counter_pokaz:
                pokaz_numb = pokaz_numb + 1
                if pokaz_numb == 1:
                    counter_con["pokaz_b"] = pokaz.value
                if pokaz_numb == counter_pokaz_len:
                    counter_con["pokaz_e"] = pokaz.value

            counter_cons.append(counter_con)

        return counter_cons