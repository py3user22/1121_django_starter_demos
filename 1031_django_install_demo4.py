#!/bin/python3


install_steps = {
    "step1": "Some steps to:\n\tInstall Django package on python @103123",
    "step1.1": "Using PS CLI on visual studio, change to directory to install & use Venv",
    "step1.2": "\tex.1031>>  cd <to directory path>",
    "step1.3": "\nCmd to start Venv: \npython -m venv <name of environment wanted>\nex1",
    "step1.4": "python -m venv 1031_django_env",
    "step1.5": "\nCmd to activate Venv: \n.\\1031_django_env\\Scripts\\activate.ps1 ",
    "step1.6": "\nCmd-line will now show green font (<Venv name>) prior to path directory",
    "step1.7": "ex2  Venv___________Path\n(1031_django_env) PS E:\\1101_django_venv_demo>",
    "step1.8": "\nInstalling & updating app(s) in (1031_django_env):",
    "step1.9": "\tpython -m pip install --upgrade pip",
    "step1.91": "\tpy -m pip install --upgrade pip",
    "step1.90": "\tpip3 install django",
    "step2.0": "----------------------",
    "step2.1": "Cmd to exit the Venv:\n\tdeactivate"
}

for kee, vaa in install_steps.items():
    print("{}".format(vaa))

next_steps = {
    "step2.2": "\nchange directory in terminal window to folder w/ manage.py",
    "step2.3": "manage.py is used to run django cmds",
    "step2.4": "\n| to run the server |>\n\tpython manage.py runserver",
    "step2.5": "| to compile the migrations |>\n\tpython manage.py makemigrations",
    "step2.6": "| to migrate the changes in database |>\n\tpython manage.py migrate",
    "step2.7": "",
    "step2.8": "",
    "step2.9": "",

}

print("<_____________________________>")
for kaa, vee in next_steps.items():
    print("{}".format(vee))

new_steps = {
    "steps3.0": "to create a django project\n\tstartproject cmd, \ncreates django project directory,",
    "steps3.1": "for given <project name> in current directory \ndefault settings: contains 'manage.py' file, & project pkg",
    "steps3.2": "ex \n\t>> django-admin startproject my_site .",
    "steps3.3": "\nTo run a project, and to start lightweight dev. web server, can be local or remote",
    "steps3.4": "ex \n\t>> python manage.py runserver",
    "steps3.5": "",
    "steps3.6": "note: Must have manage.py installed prior to using it in Venv. ",
    "steps3.7": "\nTo create a default folder structure for app of given name, --note* be in Venv",
    "steps3.8": "\n\t>> python manage.py startapp my_demoapp1031",
    "steps3.9": "\nDirectory tree shows, \\demoproject with 2 folders, demoapp, demoproject",

    "steps4.0": "\n1102 to start venv, .\\Scripts\\activate.ps1 \nwill need to be in the same folder & is case sensitive",
    "steps4.1": "",
    "steps4.2": "",
    "steps4.3": "",

}

print("<_____________________________>")
for rr, ss in new_steps.items():
    print("{}".format(ss))

