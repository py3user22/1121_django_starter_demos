#!/bin/python3


"""
Some steps to:
	Install Django package on python @103123
Using PS CLI on visual studio, change to directory to install & use Venv
	ex.1031>>  cd <to directory path>

Cmd to start Venv:
python -m venv <name of environment wanted>
ex1
python -m venv 1031_django_env

Cmd to activate Venv:
.\1031_django_env\Scripts\activate.ps1

Cmd-line will now show green font (<Venv name>) prior to path directory
ex2  Venv___________Path
(1031_django_env) PS E:\1101_django_venv_demo>

Installing & updating app(s) in (1031_django_env):
	python -m pip install --upgrade pip
	py -m pip install --upgrade pip
	pip3 install django
----------------------
Cmd to exit the Venv:
	deactivate
<_____________________________>

change directory in terminal window to folder w/ manage.py
manage.py is used to run django cmds

| to run the server |>
	python manage.py runserver
| to compile the migrations |>
	python manage.py makemigrations
| to migrate the changes in database |>
	python manage.py migrate



<_____________________________>
to create a django project
	startproject cmd,
creates django project directory,
for given <project name> in current directory
default settings: contains 'manage.py' file, & project pkg
ex
	>> django-admin startproject my_site .

To run a project, and to start lightweight dev. web server, can be local or remote
ex
	>> python manage.py runserver

note: Must have manage.py installed prior to using it in Venv.

To create a default folder structure for app of given name, --note* be in Venv

	>> python manage.py startapp my_demoapp1031

Directory tree shows, \demoproject with 2 folders, demoapp, demoproject

"""