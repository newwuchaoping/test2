import random
from datetime import datetime

from .models import UserScore, UserAnswerLog
from django.shortcuts import render
from shijuan.models import PaperList, Paper, Question, PaperCache
from django.views.generic.base import View
from user.models import UserProfile


class PaperListView(View):
    def get(self,request):
        papers = PaperList.objects.filter(is_allow=True)
         #for i in papers:
            #print(i.name, '**', i.id)
        return render(request, "paperlist.html", {"papers": papers, "title": u"试题列表页面"})
class PaperView(View):
    def get(self,request,paper_id):
        if request.user.is_authenticated :
            if  not UserScore.objects.filter(user=request.user).exists():
                papers=Paper.objects.filter(paper_name_id=paper_id)
                question_list=[]
                question_id_list=[]
                for paper in papers:
                    question=Question.objects.get(pk=paper.question_id)
                    question_list.append(question)
                    question_id_list.append(question.id)
                a = PaperList.objects.get(pk=paper_id)
                title = a.name
                question_now = tuple(question_list)
                question_count = len(question_now)
                return render(request, "test_paper.html", {"question": question_now,"question_count": question_count, "title":title})
            else:
                papers = PaperList.objects.filter(is_allow=True)
                return render(request, "paperlist.html", {"papers": papers, "title": u"试题列表页面",'msg':int(1)})
        else:
            return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户'})
    def post(self,request,paper_id):
        papers = Paper.objects.filter(paper_name_id=paper_id)
        question_id_list = []
        for paper in papers:
            question = Question.objects.get(pk=paper.question_id)
            question_id_list.append(question.id)
        user_info = UserProfile.objects.get(username=request.user)
        a = PaperList.objects.get(pk=paper_id)
        title = a.name
        user_score = UserScore()
        user_score.user = request.user
        user_score.add_time = datetime.now()
        user_score.leibie = user_info.leibie
        user_score.nickname = user_info.nickname
        user_score.danwei = user_info.danwei
        user_score.nianji = user_info.nianji
        temp_score = 0
        user_score.paper = PaperList.objects.get(pk=paper_id)
        wrong_question = []
        for i in question_id_list:
            user_ans = request.POST.get(str(i), "")
            temp_question = Question.objects.get(pk=i)
            if temp_question.answer == user_ans:
                temp_score += temp_question.score
                temp_question.cuoti='mzc'
                temp_question.save()
            else:
                question = Question.objects.get(pk=i)
                temp_question.cuoti = 'zc'
                temp_question.save()
                wrong_question.append(question)
        wrong_question_now = tuple(wrong_question)
        wrong_question_count = len(wrong_question_now)
        user_score.total = temp_score
        user_score.save()
        return render(request, "score.html", {"score": user_score.total, "title": title, "wrong_question": wrong_question_now,"wrong_question_count":wrong_question_count })
def index(request):
    userinfo = UserProfile.objects.all()
    return render(request, 'index.html', locals())


# class SelectView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             question_list = []
#             seq1 = [i for i in range(1, 4)]
#             seq2 = [i for i in range(4, 7)]
#             seq3 = [i for i in range(7, 10)]
#             question_id_list1 = random.sample(seq1, 2)
#             question_id_list2 = random.sample(seq2, 2)
#             question_id_list3 = random.sample(seq3, 2)
#             question_id_list1.extend(question_id_list2)
#             question_id_list1.extend(question_id_list3)
#             for question_id in question_id_list1:
#                 question = Question.objects.get(id=question_id)
#                 question_list.append(question)
#                 Paper_Cache = PaperCache()
#                 Paper_Cache.question = question_id
#                 Paper_Cache.user = request.user
#                 Paper_Cache.add_time = datetime.now()
#                 Paper_Cache.save()
#             title = "考试"
#             question_now = tuple(question_list)
#             question_count = len(question_now)
#             return render(request, "test_paper.html", {"question": question_now, "question_count": question_count})
#         else:
#             return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})
#
#     def post(self, request):
#         question_id_list = PaperCache.objects.filter(user=request.user)
#         user_info = UserProfile.objects.get(username=request.user)
#         title = "考试"
#         user_score = UserScore()
#         user_score.user = request.user
#         user_score.add_time = datetime.now()
#         user_score.leibie = user_info.leibie
#         user_score.nickname = user_info.nickname
#         user_score.nianji = user_info.nianji
#         user_score.danwei = user_info.danwei
#         temp_score = 0
#         user_score.paper = PaperList.objects.get(pk=3)
#         wrong_question = []
#         for i in question_id_list:
#             temp_question = Question.objects.get(pk=i.question)
#             if temp_question.questionType == 'mxz':
#                 a = str(i.question) + '_1'
#                 b = str(i.question) + '_2'
#                 c = str(i.question) + '_3'
#                 d = str(i.question) + '_4'
#                 e = str(i.question) + '_5'
#                 f = str(i.question) + '_6'
#                 user_ans1 = request.POST.get(a, "")
#                 user_ans2 = request.POST.get(b, "")
#                 user_ans3 = request.POST.get(c, "")
#                 user_ans4 = request.POST.get(d, "")
#                 user_ans5 = request.POST.get(e, "")
#                 user_ans6 = request.POST.get(f, "")
#                 user_ans_final = user_ans1 + user_ans2 + user_ans3 + user_ans4 + user_ans5 + user_ans6
#                 a = temp_question.answer
#                 if temp_question.answer == user_ans_final:
#                     temp_score += temp_question.score
#                 else:
#                     question = Question.objects.get(id=i.question)
#                     wrong_question.append(question)
#             else:
#                 user_ans = request.POST.get(str(i.question), "")
#                 if temp_question.answer == user_ans:
#                     temp_score += temp_question.score
#                 else:
#                     question = Question.objects.get(id=i.question)
#                     wrong_question.append(question)
#         wrong_question_now = tuple(wrong_question)
#         wrong_question_count = len(wrong_question_now)
#         user_score.total = temp_score
#         user_score.save()
#         question_id_list.delete()
#         return render(request, "score.html", {"score": user_score.total, "title": title, "wrong_question":wrong_question_now,"wrong_question_count":wrong_question_count })
# class TrainView(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             question_list = []
#             seq1 = [i for i in range(1, 4)]
#             seq2 = [i for i in range(4, 7)]
#             seq3 = [i for i in range(7, 10)]
#             question_id_list1 = random.sample(seq1, 2)
#             question_id_list2 = random.sample(seq2, 2)
#             question_id_list3 = random.sample(seq3, 2)
#             question_id_list1.extend(question_id_list2)
#             question_id_list1.extend(question_id_list3)
#             for question_id in question_id_list1:
#                 question = Question.objects.get(id=question_id)
#                 question_list.append(question)
#                 Paper_Cache = PaperCache()
#                 Paper_Cache.question = question_id
#                 Paper_Cache.user = request.user
#                 Paper_Cache.add_time = datetime.now()
#                 Paper_Cache.save()
#             title = "考试"
#             question_now = tuple(question_list)
#             question_count = len(question_now)
#             return render(request, "test_paper.html", {"question": question_now, "question_count": question_count, "title": title,})
#         else:
#             return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})
#
#     def post(self, request):
#         question_id_list = PaperCache.objects.filter(user=request.user)
#         title = "考试"
#         user_score = UserScore()
#         user_score.user = request.user
#         user_score.add_time = datetime.now()
#         temp_score = 0
#         user_score.paper = PaperList.objects.get(pk=3)
#         wrong_question = []
#         for i in question_id_list:
#             temp_question = Question.objects.get(pk=i.question)
#             if temp_question.questionType == 'mxz':
#                 a = str(i.question) + '_1'
#                 b = str(i.question) + '_2'
#                 c = str(i.question) + '_3'
#                 d = str(i.question) + '_4'
#                 e = str(i.question) + '_5'
#                 f = str(i.question) + '_6'
#                 user_ans1 = request.POST.get(a, "")
#                 user_ans2 = request.POST.get(b, "")
#                 user_ans3 = request.POST.get(c, "")
#                 user_ans4 = request.POST.get(d, "")
#                 user_ans5 = request.POST.get(e, "")
#                 user_ans6 = request.POST.get(f, "")
#                 user_ans_final = user_ans1 + user_ans2 + user_ans3 + user_ans4 + user_ans5 + user_ans6
#                 a = temp_question.answer
#                 if temp_question.answer == user_ans_final:
#                     temp_score += temp_question.score
#                 else:
#                     question = Question.objects.get(id=i.question)
#                     wrong_question.append(question)
#             else:
#                 user_ans = request.POST.get(str(i.question), "")
#                 if temp_question.answer == user_ans:
#                     temp_score += temp_question.score
#                 else:
#                     question = Question.objects.get(id=i.question)
#                     wrong_question.append(question)
#         wrong_question_now = tuple(wrong_question)
#         wrong_question_count = len(wrong_question_now)
#         user_score.total = temp_score
#         question_id_list.delete()
#         return render(request, "score.html",
#                       {"score": user_score.total, "title": title, "wrong_question": wrong_question_now,
#                        "wrong_question_count": wrong_question_count})

#
