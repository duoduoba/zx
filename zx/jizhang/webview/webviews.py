# coding: utf-8
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpRequest
import datetime
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from jizhang.models import UserProfile



def register(request):
	if request.method == 'PO ST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/aaa/')
	else:
		form = UserCreationForm()
	return render_to_response('registration/register.html', context={'form': form, 'context': RequestContext(request)})



def get_tags(request):
	print(request)
	now = datetime.datetime.now()
	print(now)
	t = get_template('tags.html')
	print(t)
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)


def user_profile(request):
	user = UserProfile.objects.get(user=request.user)
	city = user.city
	return {'user': request.user, 'addr': request.META['REMOTE_ADDR'], 'city': city}


def login_after(request):
	data = request.GET
	print(data)
	from django.template.context_processors import media
	from django.contrib import messages
	messages.info(request, '恭喜，你登陆成功了')
	messages.warning(request, '注意，还没有设置自己的昵称')
	return render_to_response('index.html', context_instance=RequestContext(request, processors=[user_profile, ]))


def test(request):
	print('enter test')
	print(request.GET)
	a = request.GET.get('next')
	print(type(request.GET))
	return HttpResponse("pk="+a)
