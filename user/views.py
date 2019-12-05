from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import UserProfile

from .forms import LoginForm, RegisterForm,  UserInfoForm


title='学习分析在线服务系统'
phoneNumber='123'
class LoginView(View):
    def get(self,request):
        login_form=LoginForm()
        return render(request,'login.html',{'login_form':login_form,'title':title,'phoneNumber':phoneNumber})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name=request.POST.get('username','')
            user_password=request.POST.get('password','')
            user=authenticate(username=user_name,password=user_password)
            if user is not None:
                login(request,user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request,'login.html',{"msg":"您已经成功退出登录状态" })
class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request, "register.html", {"register_form": register_form, "title": title})
    def post(self,request):
        register_form=RegisterForm(request.POST)
        if request.method=='POST':
            if register_form.is_valid():
                user_name=request.POST.get('username','')
                if UserProfile.objects.filter(username=user_name):
                    return render(request,'register.html',{'title':title,'register_form':register_form,'msg':'该账号已经被注册'})
                user_password = request.POST.get("password", "")
                user_nickname = request.POST.get("nickname", "")
                user_danwei = request.POST.get("danwei", "")
                user_email=request.POST.get('email','')
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.nickname = user_nickname
                user_profile.danwei = user_danwei
                user_profile.email = user_email
                user_profile.is_active = True
                user_profile.password = make_password(user_password)
                user_profile.save()
                return render(request, "register.html", {"title": title, "msg": u"注册成功"})
            else:
                return render(request, "register.html",{"register_form":register_form, "title": title})
        else:
            form = UserInfoForm(
                initial={

                    'danwei': '一中',
                    'leibie': '管理员',
             }
            )
            return render(request, "register.html", {"register_form": form, "title": title})
def userviews(request):
    user_form=UserInfoForm(request.POST)
    user=UserProfile.objects.get(username=request.user)
    if request.method=='POST':
        if user_form.is_valid():
            nick_name=user_form.cleaned_data['nick_name']
            birthday=user_form.cleaned_data['birthday']
            gender=user_form.cleaned_data['gender']
            leibie=user_form.cleaned_data['leibie']
            danwei = user_form.cleaned_data['danwei']
            nianji = user_form.cleaned_data['nianji']
            user.nickname = nick_name
            user.birthday = birthday
            user.gender = gender
            user.leibie = leibie
            user.danwei = danwei
            user.nianji = nianji
            user.save()
            message = '修改成功'
            return redirect('/user_center/',{'message':message})
        else:
            message = '修改失败'
            user_form = UserInfoForm()
            return render(request, 'usercenter-info.html',{'Edit_FormInput':user_form,'message':message})
    else:
        nick_name = user.nickname
        birthday = user.birthday
        gender = user.gender
        leibie = user.leibie
        danwei = user.danwei
        nianji = user.nianji
        form = UserInfoForm(
            initial={
	            'nick_name' : nick_name,
	            'birthday' : birthday,
	            'gender': gender,
	            'leibie': leibie,
	            'danwei': danwei,
	            'nianji': nianji,
            }
        )
        return render(request, 'usercenter-info.html', {'Edit_FormInput':form})

def index(request):
    userinfo = UserProfile.objects.all()
    return render(request, 'index.html', locals())

