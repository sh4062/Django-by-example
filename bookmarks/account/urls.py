from django.conf.urls import url
from django.contrib.auth.views import login
# With django 1.10 I need to pass the callable instead of 
# url(r'^login/$', 'django.contrib.auth.views.login', name='login')

from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from . import views

urlpatterns = [
    # previous login view
    #url(r'^login/$',views.user_login,name = 'login'),
    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
]