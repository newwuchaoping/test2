# -*- coding: UTF-8 –*-

import xadmin

from .models import  Video, Preview, VideoCol, Comment



class VideoAdmin(object):
    list_display = ['title', 'info', 'knowledge', 'add_time']
    search_fields = ['play_nums',  'star','knowledge' ]
    list_filter = ['title', 'info', 'knowledge', 'star',  'add_time']


class PreviewAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title']
    list_filter = ['title', 'logo', 'add_time']


class VideoColAdmin(object):
    list_display = ['video', 'user', 'add_time']
    search_fields = ['video']
    list_filter = ['video', 'user', 'add_time']


class CommentAdmin(object):
    list_display = ['content', 'add_time', 'vedio', 'user']
    search_fields = ['video', 'user']
    list_filter = ['content', 'add_time']


xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Preview, PreviewAdmin)
xadmin.site.register(VideoCol, VideoColAdmin)
xadmin.site.register(Comment, CommentAdmin)

