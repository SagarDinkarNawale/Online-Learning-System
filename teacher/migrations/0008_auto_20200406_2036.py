# Generated by Django 3.0.2 on 2020-04-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20200406_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_registration',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher_registration',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
    ]
