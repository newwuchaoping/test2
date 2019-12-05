from datetime import datetime
from django.db import models
from user.models import UserProfile
from shijuan.models import CourseList, Paper, PaperList
class UserAnswerLog(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course= models.ForeignKey(CourseList, verbose_name="课程",on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, verbose_name="试卷", on_delete=models.CASCADE)
    answer = models.TextField(verbose_name=u"用户答案")
    score = models.IntegerField(verbose_name=u"得分")
    add_time = models.DateField(default=datetime.now, verbose_name=u"作答时间")
    class Meta:
        verbose_name = u"用户做题记录"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return "{0}({1}) score={2}".format(self.user.true_name,self.user.number,self.score)
class UserScore(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    paper = models.ForeignKey(PaperList, verbose_name=u"试卷", on_delete=models.CASCADE)
    total = models.IntegerField(verbose_name=u"总分", default=0)
    add_time = models.DateField(verbose_name=u"录入时间", default=datetime.now)
    nickname = models.CharField(max_length=50, verbose_name=u"姓名", default="")
    leibie = models.CharField(verbose_name=u'类别', max_length=50, default='')
    danwei = models.CharField(verbose_name=u'单位', max_length=50, default='')
    nianji = models.CharField(verbose_name=u'年级', max_length=50, default='')
    class Meta:
        verbose_name = u"用户总分"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return "{0}({1}) 试卷:{2} | 总分:{3}".format(self.user.true_name, self.user.number, self.paper.name, self.total)
