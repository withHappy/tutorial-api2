# Generated by Django 3.0.7 on 2020-06-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
