# Generated by Django 2.1.5 on 2019-12-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stonks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stonk',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
