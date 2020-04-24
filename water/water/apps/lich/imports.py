import tkinter as tk
from tkinter import filedialog

from .models import Kotel

class ModelImport:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.txt_ = filedialog.askopenfilename()
        self.file_ = open(self.txt_, 'r')
        self.lines = self.file_.readlines()

    def lich_add(self):
        for line in self.lines:
            print(line)
        return self.lines

    def kotel_add(self):
        for line in self.lines:
            values = line.split('|')
            new_kot = Kotel(kot_kod=int(values[0]), kot_adr=values[1], kot_t_r=int(values[3]))
            new_kot.save()
            print(line + '- OK')
            
        return self.lines

    def close(self):
        self.file_.close()
        return
