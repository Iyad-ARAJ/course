# Generated by Django 3.2.25 on 2024-07-17 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
