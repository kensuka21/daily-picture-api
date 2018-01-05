# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from picture.exceptions import DailyPictureDoesNotExists


class BaseModel(models.Model):
    created_on = models.DateTimeField(null=False)
    created_by = models.CharField(null=False, max_length=100)
    update_on = models.DateTimeField(null=True)
    update_by = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.id is None:
            self.created_on = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)


class Picture(BaseModel):
    caption = models.CharField(max_length=144)
    path_url = models.CharField(max_length=250)
    user = models.ForeignKey(User, null=False)

    @classmethod
    def get_daily_picture(cls, user):
        today = date.today()

        picture = Picture.objects.filter(created_by=user,
                                         created_on__year=today.year,
                                         created_on__month=today.month,
                                         created_on__day=today.day)

        if picture.count() == 0:
            raise DailyPictureDoesNotExists('Daily picture is not uploaded.')

        return picture.latest('id')
