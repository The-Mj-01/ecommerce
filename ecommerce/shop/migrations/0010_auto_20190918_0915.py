# Generated by Django 2.2.4 on 2019-09-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190918_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='tag',
            field=models.ManyToManyField(help_text="object's tag", to='shop.Tag'),
        ),
    ]