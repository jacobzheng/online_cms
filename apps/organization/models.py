# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from common.models import BaseModel


class CityDict(BaseModel):
    desc = models.CharField(max_length=200, verbose_name=u"机构描述")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class CourseOrg(BaseModel):
    desc = models.TextField(verbose_name=u"机构描述")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to='/upload/%Y%m', verbose_name=u"封面图", default='')
    address = models.CharField(max_length=150, verbose_name=u"机构地址")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    point = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to='/upload/%Y%m', verbose_name=u"封面图", default='')
    address = models.CharField(max_length=150, verbose_name=u"机构地址")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name
