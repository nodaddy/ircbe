# Generated by Django 3.0.4 on 2020-05-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0002_auto_20200505_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='internships',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]