#!/bin/python3

"""
This is how to connect the urls.py for apps & project urls.py

urls.py aka 'routing'
"""

myapp_url = [
    '\n\t\tmyapp > urls.py ',
    'from django.urls import path',
    'from . import views',
    '\nurlpatterns = [\n\tpath("dishes/<str:dish>", views.menuitems),\n]\n ',
]


for vaa in myapp_url:
    print(vaa)
print("____________________________")

myproject_url = [
    "\n\t\tmyproject > urls.py",
    "from django.urls import path, include\n\nurlpatterns = [",
    "\tpath('', include('app_1107jg.urls')),\n]\n",
]

for vee in myproject_url:
    print(vee)
print("____________________________")

myapp_views = [
    "\n\t\tmyapp > views.py\nfrom django.http import HttpResponse\n\ndef menuitems(request, dish):\n",
    "\titems = {\n\t\t'pasta': 'Pasta is type of noodle',",
    "\t\t'falafel': 'Falafel is deep fried',",
    "\t\t'cheesecake': 'Cheesecake is a dessert',\n\t}\n",
    "\tdescription = items[dish]",
    "\treturn HttpResponse(f'<h2>{dish}</h2>' + description)",
]


for vuu in myapp_views:
    print(vuu)
print("____________________________")