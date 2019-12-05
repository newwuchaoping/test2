from datetime import datetime

from django.db import models
from user.models import UserProfile


class CourseList(models.Model):
    nianji_choices = (
        ('yinianji', '一年级'),
        ('ernianji', '二年级'),
        ('sannianji', '三年级'),
    )
    name=models.CharField(max_length=100,verbose_name='科目名',default='')
    decs=models.CharField(max_length=500,verbose_name='科目说明',default='')
    add_time=models.DateField(default=datetime.now,verbose_name='添加时间')
    nianji=models.CharField(max_length=50,verbose_name='年级',choices=nianji_choices)
    class Meta:
        verbose_name='考试科目'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Knowledge(models.Model):
    name=models.TextField(verbose_name='知识点名',default='')
    course=models.ForeignKey(CourseList,verbose_name='所属科目',on_delete=models.CASCADE)
    class Meta():
        verbose_name='知识点'
        verbose_name_plural=verbose_name
    def __str__(self):
        return  self.name
class Question(models.Model):
    course=models.ForeignKey(CourseList,verbose_name='考试科目',on_delete=models.CASCADE)
    knowledge=models.ForeignKey(Knowledge, verbose_name='所属知识点', default='', on_delete=models.CASCADE)
    questionType=models.CharField(max_length=4,choices=(('xz','选择题'),('pd','判断题'),('dxt','多选题')),default='xz',verbose_name='题目类型')
    content=models.TextField(verbose_name='题目内容')
    answer=models.TextField(verbose_name='正确答案')
    choice_a=models.TextField(verbose_name='A选项',default='A.')
    choice_b = models.TextField(verbose_name='B选项', default='B.')
    choice_c = models.TextField(verbose_name='C选项', default='C.')
    choice_d= models.TextField(verbose_name='D选项', default='D.')
    choice_e = models.TextField(verbose_name='E选项', default='E.')
    choice_f= models.TextField(verbose_name='F选项', default='F.')
    score=models.IntegerField(verbose_name='分值',default=0)
    jiexi=models.TextField(verbose_name='答案解析',default='')
    note=models.TextField(verbose_name='备注信息',default='问答题在此处做答')
    boolt=models.TextField(verbose_name='判断正误正确选项',default='对')
    boolf=models.TextField(verbose_name='判断正误错误选项',default='错')
    add_time=models.DateField(default=datetime.now,verbose_name='添加时间')
    choice_num=models.IntegerField(verbose_name='选项数',default=4)
    cuoti=models.CharField(max_length=10,verbose_name='是否做错',choices=(('zc','做错'),('mzg','没做过'),('mzc','没做错')),default='mzg')
    class Meta():
        verbose_name='题库'
        verbose_name_plural=verbose_name
    def get_content_display(self,field):
        return self.content
    def __str__(self):
        model=Question
        return "{0}(题干:{1} | 正确答案:{2} )".format(self.course.name, self.content, self.answer)
class PaperList(models.Model):
    course=models.ForeignKey(CourseList,verbose_name='所属课程',on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name='试卷名',default='')
    is_allow = models.BooleanField(default=False, verbose_name="是否启用")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = u"试卷列表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{0}(试卷名称:{1} | 使用状态:{2})".format(self.course.name, self.name, self.is_allow)
class Paper(models.Model):
    course=models.ForeignKey(CourseList,verbose_name='所属课程',default=1,on_delete=models.CASCADE)
    knowledge=models.ForeignKey(Knowledge,verbose_name='所属知识点',on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name="题目", on_delete=models.CASCADE)
    paper_name = models.ForeignKey(PaperList, verbose_name="试卷名称", on_delete=models.CASCADE)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = u"试题列表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{0} ({1})".format(self.paper_name, self.question.content)
class PaperCache(models.Model):
    question = models.IntegerField(verbose_name=u"题目")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.CASCADE)
    class Meta:
        verbose_name = u"试题临时列表"
        verbose_name_plural = verbose_name