# Generated by Django 3.1.5 on 2021-01-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210123_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='cheem_player',
            field=models.CharField(default='cheems, doge, elon musk, papu', max_length=400),
        ),
    ]