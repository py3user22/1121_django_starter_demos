#!/bin/python3


myviews_steps = {
    "step14.": "\nSteps to have your own message on the demo django webpage 110623",
    "step14.1": "\t\tmyapp > open views.py\n------------------------",
    "step14.11": "from django.http import HttpResponse\n",
    "step14.2": "def home(request):\n\treturn HttpResponse('<h1>Hola|Hello Mundo|World! by JesusG@1106. | myapp > views.py</h1>)",
    "step14.21": "-------------------------",
    "step14.3": "\n\tcreate new folder |> myapp > urls.py\n\t--------------------------",
    "step14.4": "inside the path function is where to map the URLs to its view function\n",
    "step14.5": "---------\nfrom django.urls import path\nfrom . import views",
    "step14.51": "\n\tex1..syntax\nurlpatterns = [ path(<'string to search'>, <views.<function_name>)]\n---------------",
    "step14.6": "\n\tex2.\nurlpatterns = [\n\tpath('', views.home),\n]  _________________",
    "step14.7": "\n\tex3.1104\nurlpatterns = [\n\tpath('app_1104jg/', views.home, name='home'),\n\tpath(),\n]  ________",
    "step14.8": "",
    "step14.9": "\t\t>> change to myproject folder > urls.py\n________________________\nfrom django.urls import path, include\n",
    "step15.": "urlpatterns = [\n\tpath('', include('myapp.urls')),\n]  ________________\n",
    "step15.1": "",
}

for kee, vaa in myviews_steps.items():
    print("{}".format(vaa))

