# Generated by Django 2.2 on 2021-04-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_app', '0003_auto_20210428_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]