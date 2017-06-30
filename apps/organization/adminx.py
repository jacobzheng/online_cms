# _*_ encoding:utf-8 _*_
__author__ = 'jacobzheng'
__date__ = '2017/3/31 下午4:43'

import xadmin

from .models import CourseOrg
from .models import CityDict
from .models import Teacher


class CourseOrgAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CityDictAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class TeacherAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
