# Generated by Django 3.1 on 2021-08-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210807_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
