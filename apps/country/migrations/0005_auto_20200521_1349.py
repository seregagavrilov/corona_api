# Generated by Django 2.1.7 on 2020-05-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0004_auto_20200519_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrystatistic',
            name='confirmed',
            field=models.PositiveIntegerField(null=True, verbose_name='Общее количество случаев заражения'),
        ),
        migrations.AlterField(
            model_name='countrystatistic',
            name='deaths',
            field=models.PositiveIntegerField(null=True, verbose_name='Общее количество смертей'),
        ),
        migrations.AlterField(
            model_name='countrystatistic',
            name='recovered',
            field=models.PositiveIntegerField(null=True, verbose_name='Общее количество выздоровевших'),
        ),
    ]
