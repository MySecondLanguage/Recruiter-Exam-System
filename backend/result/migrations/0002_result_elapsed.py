# Generated by Django 2.2.6 on 2019-12-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='elapsed',
            field=models.DurationField(blank=True, null=True),
        ),
    ]