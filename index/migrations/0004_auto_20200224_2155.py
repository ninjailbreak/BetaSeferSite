# Generated by Django 3.0.1 on 2020-02-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_house_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(default='Untitled', max_length=20),
        ),
    ]
