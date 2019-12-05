from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from caozuo.models import UserScore
from shijuan.models import PaperList, Paper, Question
from user.models import UserProfile


def history(request):
    if request.user.is_authenticated:
        user_info = UserProfile.objects.get(username=request.user)
        hiss = UserScore.objects.filter(user=request.user)
        return render(request, 'history.html', locals())
    else:
        return render(request, "login.html", {"msg": u'为保护用户信息，不对未登录用户开放'})
def jiexi(request,paperlist_id):
    a=PaperList.objects.get(pk=paperlist_id)
    papers=Paper.objects.filter(paper_name_id=paperlist_id)
    wrong_question_id_list = []
    for paper in papers:
        if paper.question.cuoti=='zc':
            wrong_question_id_list.append(paper.question.id)
    wrong_question = []
    for i in  wrong_question_id_list:
        question = Question.objects.get(pk=i)
        wrong_question.append(question)
    wrong_question_now = tuple(wrong_question)
    b=UserScore.objects.get(user=request.user)
    return render(request, "score.html",{'score':b.total,'title':a.name,"wrong_question": wrong_question_now})



