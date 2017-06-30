# _*_ encoding:utf-8 _*_
__author__ = 'jacobzheng'
__date__ = '2017/3/31 下午4:43'

import xadmin

from .models import Aboutus


class AboutusAdmin(object):
    list_display = ["company_profile"]

xadmin.site.register(Aboutus, AboutusAdmin)
