from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from qrcode_model.models import *
from django.http import HttpResponseRedirect


class QRView(generics.CreateAPIView):
    def get(self, request, pk):
        print('OK pk=', pk)
        q = QRData.objects.get(pk=pk)
        print(q)
        print(q.redirect)
        q.count = q.count + 1
        print('q.count=', q.count)
        q.save()
        return HttpResponseRedirect('http://' + q.redirect)