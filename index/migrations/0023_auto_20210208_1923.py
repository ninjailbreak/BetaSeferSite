# Generated by Django 3.1.1 on 2021-02-08 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_page_pagetext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagetext',
            name='Page',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='PageText',
        ),
    ]