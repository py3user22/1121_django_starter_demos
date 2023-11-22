#!/bin/python3


# view rendering template       // django > views.py
from django.shortcuts import render


def myview(request):
    if request.method == 'GET':
        # perform read or delete operation on the model

    if request.method == 'POST':
        # perform insert or update operation on the model
        context = {}  # dict containing data to be sent to the client

    return render(request, 'mytemplate.html', context)


from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self, request):
        # logic to process GET request
        return HttpResponse('response to GET request')

    def post(self, request):
        # <logic to process POST request>
        return HttpResponse('response to POST request')


