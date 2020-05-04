# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

DEPT_CHOICES = [
    ('BT', 'BioTechnology'),
]


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('first name'), max_length=100)
    dept = models.CharField(_("department"), max_length=20)
    enrl_no = models.IntegerField(_("enrollment no"), null=True)
    year = models.IntegerField(_("year"), null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_("phone number"), max_length=12)
    skype = models.CharField(_('skype name'), max_length=100)
    cv = models.CharField(_('cv'), max_length=100)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s' % self.name
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


admin.site.register(User)
