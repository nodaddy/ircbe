# Generated by Django 3.0.4 on 2020-05-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200505_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='my_applications',
            field=models.CharField(default='~', max_length=1000000, null=True, verbose_name='my_Applications'),
        ),
        migrations.AlterField(
            model_name='user',
            name='my_bookmarks',
            field=models.CharField(default='~', max_length=1000000, null=True, verbose_name='my_Bookmarks'),
        ),
    ]
