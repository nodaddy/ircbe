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
        return str(self.id) + " : " + self.name

    def __str__(self):
        return str(self.id) + " : " + self.name

    name = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=False, max_length=1000)
    deadline = models.DateTimeField(blank=False)
    status = models.CharField(_("status"), max_length=2, choices=STATUS_CHOICES)
    university = models.ForeignKey(University, related_name='internship_univ', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


admin.site.register(University)
admin.site.register(Internships)
