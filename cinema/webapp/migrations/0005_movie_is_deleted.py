# Generated by Django 2.1.7 on 2019-03-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190307_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
