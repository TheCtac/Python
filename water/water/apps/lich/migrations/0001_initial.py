# Generated by Django 3.0.4 on 2020-03-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blr_kod', models.IntegerField(verbose_name='Номер')),
                ('blr_name', models.CharField(max_length=40, verbose_name='Адреса')),
            ],
        ),
        migrations.CreateModel(
            name='diln',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diln_kod', models.IntegerField(verbose_name='Номер')),
                ('diln_name', models.CharField(max_length=40, verbose_name='Адреса')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='kms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kms_kod', models.IntegerField(verbose_name='Номер')),
                ('kms_name', models.CharField(max_length=20, verbose_name='Місце встан')),
                ('kms_name_full', models.CharField(max_length=40, verbose_name='Ремарка')),
            ],
        ),
        migrations.CreateModel(
            name='kotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kot_kod', models.IntegerField(verbose_name='Номер')),
                ('kot_adr', models.CharField(max_length=40, verbose_name='Адреса')),
                ('kot_t_r', models.IntegerField(verbose_name='Тепл.район')),
            ],
        ),
        migrations.CreateModel(
            name='lich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.IntegerField(verbose_name='Код ліч')),
                ('numb', models.CharField(max_length=20, verbose_name='Номер ліч')),
                ('typel', models.IntegerField(verbose_name='Тип ліч')),
                ('kms', models.IntegerField(verbose_name='Місце встан')),
                ('place', models.IntegerField(verbose_name="Тип об'єкта")),
                ('kotel', models.IntegerField(verbose_name='Котельня')),
                ('boiler', models.IntegerField(verbose_name='Бойлерна')),
                ('diln', models.IntegerField(verbose_name='Дільниця')),
                ('date_pov', models.DateField(verbose_name='Дата повірки')),
            ],
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_kod', models.IntegerField(verbose_name='Номер')),
                ('place_name', models.CharField(max_length=20, verbose_name="Тип об'єкта")),
            ],
        ),
        migrations.CreateModel(
            name='pokaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата показу')),
                ('kod_lich', models.IntegerField(verbose_name='Код ліч')),
                ('value', models.FloatField(verbose_name='Показ')),
            ],
        ),
        migrations.CreateModel(
            name='typel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_kod', models.IntegerField(verbose_name='Номер')),
                ('type_name', models.CharField(max_length=20, verbose_name='Тип ліч')),
                ('diam', models.IntegerField(verbose_name='Діаметр')),
                ('koef', models.FloatField(verbose_name='Коеф')),
            ],
        ),
    ]
