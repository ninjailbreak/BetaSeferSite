# Generated by Django 3.0.1 on 2020-09-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_category_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='deadline',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
