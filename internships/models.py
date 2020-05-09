from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

STATUS_CHOICES = [
    ('OP', 'Open'),
    ('UL', 'Unlisted'),
    ('DC', 'Result Declared'),
]


class University(models.Model):
    def __unicode__(self):
        return str(self.id) + " : " + self.name

    def __str__(self):
        return str(self.id) + " : " + self.name

    name = models.CharField(blank=False, max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Internships(models.Model):
    def __unicode__(self):
        return str(self.id) + " : " + self.title

    def __str__(self):
        return str(self.id) + " : " + self.title

    title = models.CharField(_('Title of the Internship __(will be treated as new internship if you edit again)'),blank=False, max_length=500, unique=True)
    description = models.TextField(blank=False, max_length=100000)
    key_tasks = models.TextField(blank=True, max_length=100000)
    critical_skills = models.TextField(blank=True, max_length=100000)
    stipend = models.CharField(blank=True, max_length=500)
    duration_in_months = models.CharField(blank=True, max_length=500)
    eligibility = models.TextField(blank=True, max_length=500)
    deadline = models.DateField(blank=False)
    status = models.CharField(_("status"), max_length=2, choices=STATUS_CHOICES)
    one_contact_email = models.EmailField(blank=False, max_length=500)
    university = models.CharField(blank=True, max_length=500)
    space_seperated_emails_of_selected_students = models.CharField(blank=True, max_length=10000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

                                
admin.site.register(University) 
admin.site.register(Internships)
