# Generated by Django 2.2.4 on 2019-09-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190913_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='published_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
