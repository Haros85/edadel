# Generated by Django 3.1 on 2020-11-19 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201119_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='unit_of_time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='unit_of_time', to='recipe.time', verbose_name='Еденица времени'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cooking_time',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(default=15, verbose_name='Время приготовления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='time',
            name='reduction',
            field=models.CharField(max_length=5, verbose_name='Сокращение'),
        ),
        migrations.AlterField(
            model_name='time',
            name='unit',
            field=models.CharField(max_length=10, verbose_name='Еденица измерения'),
        ),
        migrations.DeleteModel(
            name='CookingTime',
        ),
    ]
