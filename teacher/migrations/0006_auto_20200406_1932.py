# Generated by Django 3.0.2 on 2020-04-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20200406_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_registration',
            name='work_exp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
