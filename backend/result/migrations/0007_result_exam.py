# Generated by Django 2.2.6 on 2019-12-17 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20191217_0454'),
        ('result', '0006_auto_20191216_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Exam'),
        ),
    ]