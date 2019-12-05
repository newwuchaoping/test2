import xadmin
from .models import *
class CourseListAdmin(object):
    list_display=['name','decs','nianji','add_time']
    search_fields=['name','decs','nianji']
    list_filter=['name','decs','add_time','nianji']
class KnowledgeAdmin(object):
    list_display=['course','name']
    search_fields = ['name', 'course']
    list_filter = ['name','course']
class QuestionAdmin(object):
    list_display=['course','knowledge','questionType','score', 'content', 'answer', 'choice_a', 'choice_b',
                    'choice_c', 'choice_d', 'note', 'boolt', 'boolf','jiexi','cuoti','add_time']
    search_fields = ['course__name','knowledge', 'questionType', 'content', 'answer', 'choice_a', 'choice_b',
                     'choice_c', 'choice_d', 'note', 'boolt', 'boolf']
    list_filter = ['course', 'questionType', 'score', 'content', 'answer', 'choice_a',
                   'choice_b', 'choice_c', 'choice_d', 'note', 'boolt', 'boolf', 'add_time']
class PaperListAdmin(object):
    list_display = ['id','course','name', 'is_allow', 'add_time']
    search_fields = ['id','course__name', 'name', 'is_allow']
    list_filter = ['id','course','name', 'is_allow', 'add_time']
class PaperAdmin(object):
    list_display = ['course','knowledge','paper_name', 'question', 'add_time']
    search_fields = ['course__name','knowledge', 'paper_name__name', 'paper_name__id', 'paper_name__is_allow', 'question__id',
                     'question__content', 'question__answer']
    list_filter = ['course','knowledge', 'paper_name', 'question__id', 'question__content','add_time','paper_name__name',]
xadmin.site.register(CourseList, CourseListAdmin)
xadmin.site.register(Knowledge, KnowledgeAdmin)
xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(PaperList, PaperListAdmin)
xadmin.site.register(Paper, PaperAdmin)