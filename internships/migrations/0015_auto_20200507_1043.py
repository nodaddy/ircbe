# Generated by Django 3.0.4 on 2020-05-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0014_auto_20200506_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internships',
            name='contact_email',
        ),
        migrations.AddField(
            model_name='internships',
            name='one_contact_email',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
