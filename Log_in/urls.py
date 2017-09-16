from django.conf.urls import *
from  views import login,regist,login_test





urlpatterns=[url(r'^$',login_test),
             url(r'^regist.html',regist),
             ]

