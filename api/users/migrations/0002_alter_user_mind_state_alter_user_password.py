# Generated by Django 4.0.4 on 2022-05-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mind_state',
            field=models.CharField(blank=True, max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Password'),
        ),
    ]
