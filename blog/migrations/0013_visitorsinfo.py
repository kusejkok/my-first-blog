# Generated by Django 2.2.12 on 2020-05-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200423_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('knowDjango', models.BooleanField(default='False')),
                ('skillsDjango', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Prof', 'Prof')], default='Beginner', max_length=12)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
