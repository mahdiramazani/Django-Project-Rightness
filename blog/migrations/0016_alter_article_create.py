# Generated by Django 3.2.8 on 2022-03-24 03:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create',
            field=models.DateField(default=datetime.datetime(2022, 3, 24, 3, 19, 33, 272101, tzinfo=utc)),
        ),
    ]