# coding£ºGBK

from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpRequest
import datetime
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response



def register(request):
	if request.method == 'POST':
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
	return {'user': request.user, 'addr': request.META['REMOTE_ADDR']}


def login_after(request):
	data = request.GET
	print(data)
	from django.template.context_processors import media

	return render_to_response('index.html', {'message': 'I am the second view.'},
									context_instance=RequestContext(request, {'message': 'success login~~~'}, processors=[user_profile, ]))


def test(request):
	print('enter test')
	print(request.GET)
	a = request.GET.get('next')
	print(type(request.GET))
	return HttpResponse("pk="+a)
