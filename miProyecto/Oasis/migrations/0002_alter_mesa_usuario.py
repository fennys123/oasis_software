# Generated by Django 4.2.7 on 2024-08-05 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
