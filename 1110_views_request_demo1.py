from django.shortcuts import render
from django.http import HttpResponse


#app_1106jg  >> views.py

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    get_host = request.get_host
    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""
		<br>Path: {path}
		<br>Address: {address}
		<br>Scheme: {scheme}
		<br>Method: {method}
		<br>User agent: {user_agent}
		<br>Path info: {path_info}
		<br>Get host: {get_host}
		<br>Response header: {response.headers}

	"""
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

# return HttpResponse('<h1><i>Hola|Hello Mundo|World!</i> by JesusG<sup>@1106</sup> | myapp > views.py</h1>')


#----------------------------------------
#app_1107jg ex2
def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combo of',
        'falafel': 'Falafel are deep fried patties or balls made',
        'cheesecake': 'Cheesecake is a type of dessert made w/ ',
    }

    description = items[dish]

    return HttpResponse(f"<h2><i>{dish}</i></h2>" + description)

#----------------------------------------
#app_1107jg ex3

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)


#----------------------------------------
#app_1110 ex Using namespace in view

from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


def myview(request):
    ....
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))


#namespace in url tag
<form action="/demoapp/login" method="post">

#form attributes
<input type='submit'>
</form>

# use url tag to obtain the URL path dynamic
<form action="{% url 'login' %}" method="post">
#form attributes
<input type='submit'>
</form>

#login might be present in many apps, use the named URL w/ namespace
<form action="{% url 'demoapp:login' %}" method="post">
#form attributes
<input type='submit'>
</form>


