from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
class UserProfile(AbstractUser):
    gender_choices=(
        ('male','男'),
        ('female','女'),
    )
    leibie_choices=(
        ('guanliyuan','管理员'),
        ('jiaoshi','教师'),
        ('xuesheng','学生'),
    )
    danwei_choices=(
        ('yizhong','一中'),
        ('erzhong','二中'),
    )
    nianji_choices=(
        ('yinianji','一年级'),
        ('ernianji','二年级'),
        ('sannianji','三年级'),
    )
    nickname=models.CharField(max_length=50,verbose_name=u"姓名",default="")
    birthday=models.DateField('生日',null=True,blank=True)
    gender=models.CharField('性别',max_length=50,choices=gender_choices,default='male')
    leibie=models.CharField('类别',max_length=50,choices=leibie_choices,default='xuesheng')
    danwei=models.CharField('单位',max_length=50,choices=danwei_choices,default='')
    phone=models.CharField('电话',max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to='images/%Y%m',default='images/default.png',)
    nianji=models.CharField('年级',max_length=50,choices=nianji_choices,default='yinianji')
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码'),
        ('update_email','修改邮箱')
    )
    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=30)
    send_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name



