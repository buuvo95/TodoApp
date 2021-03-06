# Generated by Django 3.1 on 2021-08-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='category_of_todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(default='A', max_length=20),
        ),
    ]
