# Generated by Django 3.0.4 on 2020-05-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_my_applications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='my_applications',
            field=models.CharField(max_length=1000000, null=True, verbose_name='my_applications'),
        ),
    ]