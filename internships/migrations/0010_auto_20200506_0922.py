# Generated by Django 3.0.4 on 2020-05-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0009_auto_20200505_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='internships',
            name='critical_skills',
            field=models.TextField(blank=True, max_length=100000),
        ),
        migrations.AddField(
            model_name='internships',
            name='duration_in_months',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='internships',
            name='eligibility',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='internships',
            name='key_tasks',
            field=models.TextField(blank=True, max_length=100000),
        ),
        migrations.AddField(
            model_name='internships',
            name='stipend',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
