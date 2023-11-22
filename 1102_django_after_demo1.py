#!/bin/python3


""" 1102 django setup after start venv
    put your text into the default screen demo1"""

after_venv = {
    "step": "\n____________________django default message on welcome screen demo",
    "step1.": "When django project is created using | startproject |> cmd, container folder is made",
    "step1.1": "container folder will have:\nmanage.py & project pkg folder in outer folder",
    "step1.2": "\n| startapp |> cmd to create folder\n\tpython manage.py startapp <name>",
    "step1.3": "\nex1102 while in venv and folder with manage.py\n\t>> python manage.py startapp 1102demo_app",
    "step1.4": "\n1102demo_app (directory_:\n\t|--> admin.py\n\t|--> apps.py",
    "step1.5": "\t|--> models.py\n\t|--> tests.py\n\t|--> views.py\n\t|--> __init__.py",
    "step1.50": "\t|--> urls.py       *create new file",
    "step1.6": "\t|\n\t|__> migrations __> __init__.py",
    "step1.7": "\nex.1102 ______| views.py |_______\nview.py is user-defined function thats called when:",
    "step1.8": "URL dispatcher identifies  the clients request URL\n\tand matches it w/ URL pattern defined in | urls.py |",
    "step1.9": "note: default autosetting for views.py is empty",

    "step12.": "\n\t\tex2 __> adding views.py function called index()",
    "step1.91": "\t\t-----------------------------------------",
    "step1.92": "from django.http import HttpResponse",
    "step12.1": "def index(request):\n\treturn HttpResponse('Aloha, world. This is index view of 1102demo_app') ",
    "step12.2": "\n\t\t______| urls.py |______\n-> defines URL patterns for the project",
    "step12.3": "-> app folder will not have urls.py, create new one",
    "step12.4": "\n\t\tex __> putting the path to views\n\t\t--------------------------------",
    "step12.5": "from django.urls import path, include\nfrom . import views\n",
    "step12.51": "syntax for path()\n\t>> path(route, view, kwargs=None, name=None)",
    "step12.52": "\n\tex. __> \nurlpatterns2 = [\n\tpath('index/', views.index, name='')",
    "step12.53": "\tpath('bio/<username>/', views.bio, name='bio'),",
    "step12.54": "\tpath('blog/', include('blog.urls')), ]\n",


    "step12.6": "urlpatterns = [\n\tpath('', views.index, name='index'),\n]\n---------------------",
    "step12.7": "\n1102demo_project (directory_:\n\t|--> asgi.py\n\t|--> settings.py\n\t|--> urls.py",
    "step12.8": "\t|--> wsgi.py\n\t|--> __init__.py\n",
    "step12.9": "Next, update | urlpatterns | list in project folder | urls.py | and include app URL configuration",

    "step13.": "\n\t\tex1102 __> 1102demo_project/urls.py",
    "step13.1": "from django.contrib import admin\nfrom django.urls import include, path",
    "step13.2": "\nurlpatterns = [\n\tpath('demo/', include('demoapp.urls')),",
    "step13.3": "\tpath('admin/', admin.site.urls),\n]\n",
    "step13.4": "\t\tex __> update settings.py\nupdate list of INSTALLED_APPS [] section",
    "step13.5": "add the name of <demoapp> at bottom of list, ...', 'demoapp', ]",
    "step13.6": "",
    "step13.7": "",
    "step13.8": "",
    "step13.9": "",
}

"""
    "step14.": "",
    "step14.1": "",
    "step14.2": "",
    "step14.3": "",
    "step14.4": "",
    "step14.5": "",
    "step14.6": "",
    "step14.7": "",
    "step14.8": "",
    "step14.9": "",

    "step15.": "",
    "step15.1": "",
"""

for kee, vaa in after_venv.items():
    #print("\t{}\n{}".format(kee, vaa))
    print("{}".format(vaa))
