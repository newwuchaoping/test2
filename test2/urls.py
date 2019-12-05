"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from caozuo.views import PaperListView, PaperView
from django.conf.urls import url
from django.urls import path, include
from fenxi.views import AnimationView
from shijuan.views import history, jiexi
from user.views import LoginView,RegisterView,LogoutView,userviews,index
from django.views.static import serve
from test2.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path(r'^captcha/', include('captcha.urls')),
    path('login/', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(),name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_center/', userviews, name="user_center"),
    path('index/', index,name="index"),
    path('paperlist/', PaperListView.as_view(), name="paper_list"),
    path('paper/<paper_id>/', PaperView.as_view(), name="paper"),
    path('history/', history, name="history"),
    path('jiexi/<paperlist_id>',jiexi, name="jiexi"),
    url(r'^animation/$', AnimationView.as_view(), name='animation'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]
