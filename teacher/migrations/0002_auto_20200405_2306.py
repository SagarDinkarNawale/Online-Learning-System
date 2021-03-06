# Generated by Django 3.0.2 on 2020-04-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_registration',
            name='description',
        ),
        migrations.RemoveField(
            model_name='teacher_registration',
            name='designation',
        ),
        migrations.AddField(
            model_name='teacher_registration',
            name='about',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_registration',
            name='profile_photo',
            field=models.ImageField(default=0, upload_to='teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_registration',
            name='work_exp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher_registration',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher_registration',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
