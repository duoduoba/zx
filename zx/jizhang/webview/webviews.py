# coding: utf-8
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpRequest
import datetime
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from jizhang.models import UserProfile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from jizhang.models import SpendDetail, UserProfile
from rest_framework import permissions
from jizhang.log.logger import logger
from django.template import Template, Context, RequestContext


class WebSpendList(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'share.html'
	permission_classes = (permissions.AllowAny,)

	def get(self, request):
		uuid = request.GET.get('id', None)
		try:
			logger.info('id={}'.format(uuid))
			up = UserProfile.objects.get(uuid=uuid)
			user = up.user
			details_list = SpendDetail.objects.filter(owner=user)
			logger.info(details_list)
			return Response(locals())
		except:
			logger.info('export spend detail list to web happened error')
			raise Http404

	def post(self, request):
		# 生成分享web页面
		user = request.user
		try:
			up = UserProfile.objects.filter(user=user)
			if not up.uuid:
				import uuid
				uid = uuid.uuid5(uuid.NAMESPACE_DNS, self.request.user.username + "." + str(self.request.user.id))
				up.uuid = uid
				up.save()
				# uid = uuid.uuid5(uuid.NAMESPACE_DNS, self.request.user.username + "." + str(self.request.user.id))
			t = Template('share')
		except:
			logger.info('create share.html error')
			return Response(status=status.HTTP_400_BAD_REQUEST)



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
	print(request.user)
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



