# Generated by Django 3.0.4 on 2020-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0006_auto_20200505_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internships',
            old_name='University',
            new_name='university',
        ),
        migrations.AlterField(
            model_name='internships',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='internships',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='internships',
            name='deadline',
            field=models.DateField(),
        ),
    ]