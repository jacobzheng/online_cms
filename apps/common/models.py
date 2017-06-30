# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


class BaseModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名称",default="")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        abstract = True
