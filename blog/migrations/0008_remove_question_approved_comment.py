# Generated by Django 2.2.12 on 2020-04-07 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_question_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='approved_comment',
        ),
    ]