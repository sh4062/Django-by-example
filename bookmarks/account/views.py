from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm
# Create your views here.
###
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
###
from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,
                 'account/dashboard.html',
                 {'section': 'dashboard'})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username = cd['username'],
#                                 password = cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:form = LoginForm()
#     return render(request,'account/login.html',{'form':form})
