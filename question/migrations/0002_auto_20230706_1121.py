# Generated by Django 3.2.10 on 2023-07-06 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedanswers',
            name='match_id',
        ),
        migrations.DeleteModel(
            name='MatchCreated',
        ),
    ]
