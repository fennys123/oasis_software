# Generated by Django 5.1.1 on 2024-10-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0008_entradasqr'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
