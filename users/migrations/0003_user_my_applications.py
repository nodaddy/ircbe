# Generated by Django 3.0.4 on 2020-05-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200505_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='my_applications',
            field=models.CharField(max_length=1000, null=True, verbose_name='my_applications'),
        ),
    ]