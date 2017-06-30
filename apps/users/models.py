# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

SEX_CHOICES = (
    ('male', u'男'),
    ('female', u'女')
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateTimeField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=SEX_CHOICES, verbose_name=u"性别",
                              default="female")
    address = models.CharField(max_length=500, verbose_name=u"地址", default="")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号", default="")
    image = models.ImageField(upload_to='/upload/%Y%m', verbose_name=u"头像", default='')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10)
    send_date = models.DateTimeField(default=datetime.now, verbose_name=u"发送日期")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题", default="")
    image = models.ImageField(upload_to='/upload/%Y%m', verbose_name=u"封面图", default='')
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
