# Generated by Django 3.2.10 on 2023-07-05 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competion', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchCreated',
            fields=[
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competion.competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=255)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('correct_ans', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SavedAnswers',
            fields=[
                ('saved_answers_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer_time', models.IntegerField()),
                ('Participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.participant')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competion.competition')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.matchcreated')),
            ],
        ),
    ]
