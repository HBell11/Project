# Generated by Django 5.0.4 on 2024-04-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_rainpercent_wind'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='forecastdata',
            name='fnx',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='forecastdata',
            name='fny',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rainpercent',
            name='fnx',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rainpercent',
            name='fny',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wind',
            name='fnx',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wind',
            name='fny',
            field=models.IntegerField(default=0),
        ),
    ]
