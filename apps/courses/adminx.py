# _*_ encoding:utf-8 _*_
__author__ = 'jacobzheng'
__date__ = '2017/3/31 下午4:43'

import xadmin

from .models import Course
from .models import Lesson
from .models import Video
from .models import CourseResource


class CourseAdmin(object):
    list_display = ["name", "desc"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "type"]


class LessonAdmin(object):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


class VideoAdmin(object):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


class CourseResourceAdmin(object):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
