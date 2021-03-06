# Generated by Django 3.1 on 2020-12-13 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0006_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for_list', to='recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopper', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
