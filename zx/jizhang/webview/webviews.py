__author__ = 'zx'
# coding£ºutf-8

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime


def get_tags(request):
	print(request)
	now = datetime.datetime.now()
	print(now)
	t = get_template('tags.html')
	print(t)
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

