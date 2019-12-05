from datetime import datetime

from django.db import models

# Create your models here.
from shijuan.models import Knowledge
from user.models import UserProfile


class Video(models.Model):
    title=models.CharField(max_length=200,verbose_name="课程标题")
    movie_file=models.FileField(max_length=200,upload_to='video/%Y/%m',default="videos/default.mp4",verbose_name='视频文件')
    info=models.TextField(verbose_name='视频简介',default='')
    logo=models.ImageField(upload_to='banner/%Y/%m',default='image/default.img',max_length=100,verbose_name='封面')
    star = models.IntegerField(verbose_name='星级')
    play_nums = models.IntegerField(verbose_name='播放量')
    comment_nums = models.IntegerField(verbose_name='评论数')
    length = models.CharField(max_length=200, verbose_name='时长')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    knowledge=models.ForeignKey(Knowledge,on_delete=models.CASCADE,verbose_name='所属知识点')
    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
class Comment(models.Model):
    content = models.TextField(verbose_name="评论详情", default='')
    vedio = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='视频')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name
class VideoCol(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='视频')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '用户收藏'
class Preview(models.Model):
    title = models.CharField(max_length=200, verbose_name='视频标题')
    logo = models.ImageField(upload_to='banner/%Y/%m', default='image/default.png', max_length=100, verbose_name='封面')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '推荐预告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title