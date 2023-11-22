#!/bin/python3

""" w2_lab2_mapping urls w/ parameters
You have already built the project named myproject and added an app inside the project called myapp.

The settings inside the settings.py file is already updated and at:
project-level, urls.py is updated with reference to the app-level URL configuration.

urls list w/ the following parameters:
1- path string starting w/ suffix 'drinks/'
    followed by < string path converter >   that has variable called drink_name
              str:  var1
>>   'drinks/<str:drink_name>'

Note: 1107 for emojis add to script >> win key + ;  or  win + .

make sure to import the views.py, & the path function from django.urls pkg.

"""

create_drinks = {
    "step1.": "\n\tSteps to make views show different webpage, on URL changes",
    "step1.1": "myapp > urls.py | create file & add the function path() inside the list\n",
    "step1.2": "urlpatterns = [\n\tpath('drinks/<str:drink_name>', views.drinks, name='drink_name'),\n]\n ",
    "step1.3": "\tmyapp > views.py\ncreate function called 'drinks' w/ 2 arguments (request, drink_name)",
    "step1.4": "\ndef drinks (request, drink_name):\n\tdrinks = {\n\t\t'mocha': 'type of coffee',",
    "step1.5": "\t\t'tea': 'type of beverage',\n\t\t'lemonade': 'type of refreshment',\n\t}\n",
    "step1.6": "Create variable called 'choice_of_drink',\nassign value of 'drink_name' by passing it inside dictionary",
    "step1.7": "\nchoice_of_drink = <dict key value> ",
    "step1.8": "",
    "step1.9": "",
    "step1.11": "",
    "step1.12": "",
    "step1.13": "",
    "step1.14": "",

}

for kee, vaa in create_drinks.items():
    print("{}".format(vaa))

