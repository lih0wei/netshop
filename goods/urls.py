#-*- codeing = utf-8 -*-
#@Time : 2021/2/5  10:28
#@Aythor : LHW 
#@File : urls.py
#@Software: PyCharm
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.IndexView.as_view()),
    url(r'^category/(\d+)$', views.IndexView.as_view()),
    url(r'^category/(\d+)/page/(\d+)$', views.IndexView.as_view()),
    url(r'^goodsdetails/(\d+)$', views.DetailView.as_view()),
]
