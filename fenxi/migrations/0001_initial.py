# Generated by Django 2.0 on 2019-12-04 02:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shijuan', '0003_question_cuoti'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', verbose_name='评论详情')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户评论',
                'verbose_name': '用户评论',
            },
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='视频标题')),
                ('logo', models.ImageField(default='image/default.png', upload_to='banner/%Y/%m', verbose_name='封面')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '推荐预告',
                'verbose_name': '推荐预告',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='课程标题')),
                ('movie_file', models.FileField(default='videos/default.mp4', max_length=200, upload_to='video/%Y/%m', verbose_name='视频文件')),
                ('info', models.TextField(default='', verbose_name='视频简介')),
                ('logo', models.ImageField(default='image/default.img', upload_to='banner/%Y/%m', verbose_name='封面')),
                ('star', models.IntegerField(verbose_name='星级')),
                ('play_nums', models.IntegerField(verbose_name='播放量')),
                ('comment_nums', models.IntegerField(verbose_name='评论数')),
                ('length', models.CharField(max_length=200, verbose_name='时长')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('knowledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shijuan.Knowledge', verbose_name='所属知识点')),
            ],
            options={
                'verbose_name_plural': '视频信息',
                'verbose_name': '视频信息',
            },
        ),
        migrations.CreateModel(
            name='VideoCol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fenxi.Video', verbose_name='视频')),
            ],
            options={
                'verbose_name': '用户收藏',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fenxi.Video', verbose_name='视频'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]