# Generated by Django 4.0.3 on 2022-03-18 00:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 0, 42, 18, 123853, tzinfo=utc)),
        ),
    ]
