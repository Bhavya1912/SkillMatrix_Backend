# Generated by Django 3.2.10 on 2023-07-17 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_participant_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='user.participant'),
        ),
    ]