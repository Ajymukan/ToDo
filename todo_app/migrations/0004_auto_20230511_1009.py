# Generated by Django 3.2.12 on 2023-05-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20230511_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='create_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='update_data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
