# Generated by Django 3.0.1 on 2020-09-25 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20200925_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]