# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

from django.db import models

from common.models import BaseModel


# Create your models here.

COURSE_LEVEL_CHOICES = (
    ('cj', '初级'),
    ('zj', '中级'),
    ('gj', '高级'),
)

COURSE_TYPE_CHOICES = (
    ('wlb', '网络班'),
    ('spb', '视频班'),
    ('msb', '面授班')
)


class Course(BaseModel):
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(choices=COURSE_LEVEL_CHOICES, max_length=2, verbose_name=u"课程难度")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    imageFile = models.ImageField(upload_to='/upload/%Y%m', verbose_name=u"封面图", default='')
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    type = models.CharField(choices=COURSE_TYPE_CHOICES, max_length=5, verbose_name=u"课程类型", default='')

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, verbose_name=u"课程")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    video_link = models.FileField(upload_to='/upload/%Y%m', verbose_name=u"视频地址", default='')

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, related_name='course_name', verbose_name=u"课程")
    resource_link = models.FileField(upload_to='/upload/%Y%m', verbose_name=u"资源文件", default='')

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
