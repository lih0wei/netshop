#-*- codeing = utf-8 -*-
#@Time : 2021/2/7  16:36
#@Aythor : LHW 
#@File : urls.py
#@Software: PyCharm
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.RegisterView.as_view()),
    url(r'^checkUname/$', views.CheckUnameView.as_view()),
    url(r'^center/$', views.CenterView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^loadCode.jpg$', views.LoadCodeView.as_view()),
    url(r'^checkcode/$', views.CheckCodeView.as_view()),
    url(r'^address/$', views.AddressView.as_view()),
    url(r'^loadArea/$', views.LoadAreaView.as_view()),
]
