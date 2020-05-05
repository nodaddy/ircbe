# Generated by Django 3.0.4 on 2020-05-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internships',
            name='name',
        ),
        migrations.AddField(
            model_name='internships',
            name='title',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='internships',
            name='description',
            field=models.TextField(max_length=100000),
        ),
    ]