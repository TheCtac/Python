# Generated by Django 3.0.4 on 2020-04-28 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lich', '0014_auto_20200428_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='diln',
            name='master',
            field=models.CharField(blank=True, max_length=30, verbose_name='Майстер'),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='kotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lich.Kotel', verbose_name='Котельня'),
        ),
        migrations.AlterField(
            model_name='lich',
            name='boiler',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='lich.Boiler', verbose_name='Бойлерна'),
        ),
        migrations.AlterField(
            model_name='lich',
            name='diln',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lich.Diln', verbose_name='Дільниця'),
        ),
        migrations.AlterField(
            model_name='lich',
            name='kms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lich.Kms', verbose_name='Місце встан'),
        ),
        migrations.AlterField(
            model_name='lich',
            name='kotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lich.Kotel', verbose_name='Котельня'),
        ),
        migrations.AlterField(
            model_name='lich',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lich.Place', verbose_name="Тип об'єкта"),
        ),
        migrations.AlterField(
            model_name='lich',
            name='typel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lich.Typel', verbose_name='Тип ліч'),
        ),
        migrations.AlterField(
            model_name='pokaz',
            name='kod_lich',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lich.Lich', verbose_name='Код ліч'),
        ),
    ]
