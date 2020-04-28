from django.db import models

class Typel(models.Model):
    type_kod = models.IntegerField('Номер', primary_key=True)
    type_name = models.CharField('Тип ліч', max_length=20)
    diam = models.IntegerField('Діаметр', blank = True)
    koef = models.FloatField('Коеф')
    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name = "Тип лічильника"
        verbose_name_plural = "Типи лічильників"

class Kms(models.Model):
    kms_kod = models.IntegerField('Номер', primary_key=True)
    kms_name = models.CharField('Місце встан', max_length=20)
    kms_name_full = models.CharField('Ремарка', max_length=40, blank = True)
    def __str__(self):
        return self.kms_name_full
    class Meta:
        verbose_name = "Місця встановлення"
        verbose_name_plural = "Місця встановлення"

class Place(models.Model):
    place_kod = models.IntegerField('Номер', primary_key=True)
    place_name = models.CharField('Тип об\'єкта', max_length=20)
    def __str__(self):
        return self.place_name
    class Meta:
        verbose_name = "Тип об'єкту"
        verbose_name_plural = "Типи об'єктів"

class Kotel(models.Model):
    kot_kod = models.IntegerField('Номер', primary_key=True)
    kot_adr = models.CharField('Адреса', max_length=40)
    kot_t_r = models.IntegerField('Тепл.район')
    def __str__(self):
        return self.kot_adr
    class Meta:
        verbose_name = "Котельня"
        verbose_name_plural = "Котельні"

class Boiler(models.Model):            
    blr_kod = models.IntegerField('Номер', primary_key=True)
    blr_name = models.CharField('Адреса', max_length=40)
    kotel = models.ForeignKey(Kotel, on_delete=models.CASCADE, verbose_name='Котельня')
    def __str__(self):
        return self.blr_name
    class Meta:
        verbose_name = "ЦТП"
        verbose_name_plural = "ЦТП"

class Diln(models.Model):   
    diln_kod = models.IntegerField('Номер', primary_key=True)
    diln_name = models.CharField('Адреса', max_length=40)
    phone = models.CharField('Телефон', max_length=10, blank = True)
    master = models.CharField('Майстер', max_length=30, blank = True)
    def __str__(self):
        return self.diln_name
    class Meta:
        verbose_name = "Дільниця"
        verbose_name_plural = "Дільниці"

class Lich(models.Model):
    date_open = models.DateField('Початкова дата')
    date_close = models.DateField('Кінцева дата', blank = True)
    kod = models.IntegerField('Код ліч', primary_key=True)
    numb = models.CharField('Номер ліч', max_length=20)
    typel = models.ForeignKey(Typel, on_delete=models.PROTECT, verbose_name='Тип ліч')
    kms = models.ForeignKey(Kms, on_delete=models.PROTECT, verbose_name='Місце встан')
    place = models.ForeignKey(Place, on_delete=models.PROTECT, verbose_name='Тип об\'єкта')
    kotel = models.ForeignKey(Kotel, on_delete=models.PROTECT, verbose_name='Котельня')
    boiler = models.ForeignKey(Boiler, on_delete=models.PROTECT, verbose_name='Бойлерна', blank = True)
    diln = models.ForeignKey(Diln, on_delete=models.PROTECT, verbose_name='Дільниця')
    date_pov = models.DateField('Дата повірки')
    def __str__(self):
        return str(self.kod) + ' - ' + self.numb 
    class Meta:
        verbose_name = "Лічильник"
        verbose_name_plural = "Лічильники"

class Pokaz(models.Model):
    date = models.DateField('Дата показу')
    kod_lich = models.ForeignKey(Lich, on_delete=models.PROTECT, verbose_name='Код ліч')
    value = models.FloatField('Показ')
    def __str__(self):
        return str(self.kod_lich) + ' - ' + str(self.date) 
    class Meta:
        verbose_name = "Показ"
        verbose_name_plural = "Покази"
    
class Menu_item(models.Model):
    menu_id = models.IntegerField('Код меню', primary_key=True)
    menu_name = models.CharField('Назва', max_length=30)
    url_link = models.CharField('Шлях', max_length=50, blank = True)
    parent_id = models.IntegerField('Головне меню')

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункти меню"
    def __str__(self):
        return  str(self.menu_id) + '.' + str(self.menu_name)
