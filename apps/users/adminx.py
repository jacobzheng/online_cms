# _*_ encoding:utf-8 _*_
__author__ = 'jacobzheng'
__date__ = '2017/3/31 下午4:43'

import xadmin

from xadmin import views

from .models import UserProfile
from .models import Banner
from .models import EmailVerifyRecord


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "AMC-China CMS"
    site_footer = "上海棒呆力教育科技有限公司"


class UserProfileAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class BannerAdmin(object):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


class EmailVerifyRecordAdmin(object):
    list_display = ['code']
    search_fields = ['code']
    list_filter = ['code']

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
