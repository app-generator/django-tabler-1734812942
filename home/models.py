# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Semester(models.Model):

    #__Semester_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Semester_FIELDS__END

    class Meta:
        verbose_name        = _("Semester")
        verbose_name_plural = _("Semester")


class Teacher(models.Model):

    #__Teacher_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    department = models.TextField(max_length=255, null=True, blank=True)
    siape = models.TextField(max_length=255, null=True, blank=True)

    #__Teacher_FIELDS__END

    class Meta:
        verbose_name        = _("Teacher")
        verbose_name_plural = _("Teacher")


class Discipline(models.Model):

    #__Discipline_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)

    #__Discipline_FIELDS__END

    class Meta:
        verbose_name        = _("Discipline")
        verbose_name_plural = _("Discipline")


class Class(models.Model):

    #__Class_FIELDS__
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    time = models.TextField(max_length=255, null=True, blank=True)
    local = models.TextField(max_length=255, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    #__Class_FIELDS__END

    class Meta:
        verbose_name        = _("Class")
        verbose_name_plural = _("Class")


class Distribution(models.Model):

    #__Distribution_FIELDS__
    class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    hours = models.IntegerField(null=True, blank=True)

    #__Distribution_FIELDS__END

    class Meta:
        verbose_name        = _("Distribution")
        verbose_name_plural = _("Distribution")



#__MODELS__END
