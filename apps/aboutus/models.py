# _*_ encoding:utf-8 _*_


from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class Aboutus(models.Model):
    company_profile = HTMLField(verbose_name=u"公司简介")
    teachers = HTMLField(verbose_name=u"师资介绍")
    achievement = HTMLField(verbose_name=u"培训成就")
    course_description = HTMLField(verbose_name=u"课程介绍")
    course_type = HTMLField(verbose_name=u"课程类型")
    course_content = HTMLField(verbose_name=u"课程内容")
    main_course = HTMLField(verbose_name=u"主要课程")

    class Meta:
        verbose_name=u"关于我们"
        verbose_name_plural = verbose_name
