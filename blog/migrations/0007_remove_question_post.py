# Generated by Django 2.2.12 on 2020-04-07 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200407_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='post',
        ),
    ]