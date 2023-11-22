#!/bin/python3


# myapp > url.py

#      search string      , views.<method name>,
path('getuser/<name>/<id>', views.pathview, name='pathview'),
path('getuser/', views.qryview, name='qryview'),
path("showform/", views.showform, name="showform"),
path("getform/", views.getform, name='getform'),


# add pathview() function in ... apps> views.py

from django.http import HttpResponse

def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse("Name:{} UserID:{}".format(name, id))


# save as form.html >> templates directory
"""
<form action="/myapp/getform/" method="POST">
    {% csrf_token %}                        # {% csrf_token %} tag is necessary to prevent cross-site forgery attacks.
    <p>Name: <input type="text" name="id"></p>
    <p>UserID :<input type="name" name="name"></p>
    <input type="submit">
</form>
"""
#------------------------

