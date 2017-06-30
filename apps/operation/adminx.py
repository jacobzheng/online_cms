# _*_ encoding:utf-8 _*_
__author__ = 'jacobzheng'
__date__ = '2017/3/31 下午4:43'

import xadmin

from .models import UserAsk
from .models import UserMessage
from .models import CourseComments
from .models import UserFavorite
from .models import UserCourse


class UserAskAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class UserMessageAdmin(object):
    list_display = ['message']
    search_fields = ['message']
    list_filter = ['message']


class UserFavoriteAdmin(object):
    list_display = ['fav_type']
    search_fields = ['fav_type']
    list_filter = ['fav_type']


class CourseCommentsAdmin(object):
    list_display = ['comments']
    search_fields = ['comments']
    list_filter = ['comments']


class UserCourseAdmin(object):
    list_display = ['course']
    search_fields = ['course']
    list_filter = ['course']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
