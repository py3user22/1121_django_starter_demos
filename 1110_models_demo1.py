#!/bin/python3


# app > models.py

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " : " + self.cuisine

# ===============================>

"""
1- go in terminal w/ directory that has manage.py

2- >> python manage.py makemigrations
3- >> python manage.py migrate

4- >> python manage.py shell        # now in py3 shell terminal

>> from app4_1110jg.models import Menu
>> Menu.objects.all()
>> m = Menu.objects.create(name = 'pasta', cuisine = 'italian', price = 10)
>> n = Menu.objects.create(name = 'taco', cuisine = 'mexican', price = 2)
>> Menu.objects.all()
<QuerySet [<Menu: Menu object (1)>, <Menu: Menu object (2)>]>

>> exit()   # to exit the shell

>>> from app4_1110jg.models import Menu
>>> p = Menu.objects.get(pk=2)
>>> p.cuisine = 'chinese'
>>> p.save
<bound method Model.save of <Menu: Menu object (2)>>
>>> Menu.objects.all()
<QuerySet [<Menu: Menu object (1)>, <Menu: Menu object (2)>]>
>>> exit()
"""

# ex2 1111 1-to-1 relationship, primary key is CollegeID


class College(models.Model):
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website = models.URLField()


class Principal(models.Model):
    CollegeID = models.OneToOneField(
                College,
                on_delete=models.CASCADE
                )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

"""
In the principal model, you must provide the CollegeID field as the foreign key.
The on_delete option specifies the behavior in case the associated object in the primary model is deleted.
The values are:

CASCADE: deletes the object containing the ForeignKey

PROTECT: Prevent deletion of the referenced object.

RESTRICT: Prevent deletion of the referenced object by raising RestrictedError

The principal model has the following field structure:
"""


# 1-to-many relationship
class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key = True)       # primary key
    name = models.CharField(max_length=30)
    credits = models.IntegerField()


class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)           # primary key
    Subjectcode=models.ForeignKey(                              # foreign key
                Subject,
                on_delete=models.CASCADE
                  )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


