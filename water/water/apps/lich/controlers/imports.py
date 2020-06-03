import tkinter as tk
from tkinter import filedialog
from datetime import datetime

from lich.models import Kotel, Boiler, Typel, Diln, Lich, Place, Kms

class ModelImport:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.txt_ = filedialog.askopenfilename()
        self.file_ = open(self.txt_, 'r')
        self.lines = self.file_.readlines()

    def lich_add(self):
        for line in self.lines:
            values = line.split('|')
            typel_ = Typel.objects.get(pk=int(values[2]))
            kms_ = Kms.objects.get(pk=int(values[3]))
            place_ = Place.objects.get(pk=int(values[4]))
            kotel_ = Kotel.objects.get(pk=int(values[5]))
            boiler_ = Boiler.objects.get(pk=int(values[6]))
            diln_ = Diln.objects.get(pk=int(values[7]))
            date_ = datetime.strptime(values[8], '%d.%m.%Y')

            new_lich = Lich(
                date_open='2020-04-01',
                kod=int(values[0]),
                numb=values[1],
                typel=typel_,
                kms=kms_,
                place=place_,
                kotel=kotel_,
                boiler=boiler_,
                diln=diln_,
                date_pov=date_
            )
            new_lich.save()
            print(line + '- OK')
        return self.lines

    def kotel_add(self):
        for line in self.lines:
            values = line.split('|')
            new_kot = Kotel(kot_kod=int(values[0]), kot_adr=values[1], kot_t_r=int(values[3]))
            new_kot.save()
            print(line + '- OK')
            
        return self.lines

    def boiler_add(self):
        for line in self.lines:
            values = line.split('|')
            kotel_ = Kotel.objects.get(pk=int(values[3]))
            new_boiler = Boiler(blr_kod=int(values[0]), blr_name=values[1], kotel=kotel_)
            new_boiler.save()
            print(line + '- OK')
            
        return self.lines

    def lich_type_add(self):
        for line in self.lines:
            values = line.split('|')
            new_type = Typel(type_kod=int(values[0]), 
                             type_name=values[1], 
                             diam=int(values[3]), 
                             koef=float(values[4]))
            new_type.save()
            print(line + '- OK')
            
        return self.lines
        
    def diln_add(self):
        for line in self.lines:
            values = line.split('|')
            new_diln = Diln(diln_kod=int(values[0]), 
                            diln_name=values[1], 
                            phone='', 
                            master=values[2])
            new_diln.save()
            print(line + '- OK')
            
        return self.lines
    def close(self):
        self.file_.close()
        return
