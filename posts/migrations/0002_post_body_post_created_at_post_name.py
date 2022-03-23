# Generated by Django 4.0.3 on 2022-03-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=140, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Created DateTime'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name'),
        ),
    ]
