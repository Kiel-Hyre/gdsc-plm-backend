## About GDSC-PLM-BACKEND
- A series of activities provided to learn Django as a whole and as a backend

## Requirements
* [pip3](https://www.python.org/)
* [virtualenv](https://pypi.org/project/virtualenv/)
* [django](https://pypi.org/project/Django/)


## Setup
* Virtual Environment

1. Use virtualenv to add a virtual environment
```
    virtualenv venv
```
2. Activate the environment
```
    venv/Scripts/activate/
```
3. Deactivate enviroment
```
    deactivate
```

* Install requirements for python3
1. (Optional) Upgrade Tools
```
    pip3 install --upgrade setuptools #pip only for Windows
```
2. (Optional) Upgrade Pip
```
    python3 -m pip install --upgrade pip #python only for Windows unless there is other version
```
3. Install requirements in requirements.txt
```
    pip3 install -r requirements.txt
```

* Environment Variables
1. In source folder aligned with manage.py create **.env** file
```
    app\
        ... # other files
        .env
```

* Start a project
```
    django-admin startproject <your-app>
    e.g django-admin startproject config
```
This will create a folder named config containing all necessary items e.g manage.py

To create in the same base of gdsc-plm-backend do:
```
    django-admin startproject config . #there is a dot
```

* Common Commands for Django

1. Makemigrations
```
    python3 manage.py makemigrations
```
2. Migrate Applications
```
    python3 manage.py migrate
```
3. More django commands [info](https://www.djangoproject.com/)


## Run Servers

1. Run server for Django
```
    python3 manage.py runserver (port) # default is 8000
```

## BACKEND-01-HELLO WORLD

- Create your app
In main directory (gdsc-plm-backend/)

```
django-admin startapp hello
```

- It should contain the basics files of an app
```
e.g
hello\
    migrations\
    admin.py
    ...etc
```

- Put your app in the settings.py INSTALLED_APPS
```
INSTALLED_APPS = [
    ...
    hello
]
```

- Create a urls.py on your hello folder
- It should contains this
```
from django.urls import path

urlpatterns = [
    # put your routes here
]

```

- To be recognized hello app urls it should be detected in the urls.py on the config folder
- It can be done like this
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')) # this includes all the routes provided by the hello app
]
```

- Now we had our routes file prepared, lets make some views
- Create a view function named hello
```
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")
```

- Create a route based on that view
```
hello/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.hello, name='hello-index')
]
```

### TADA YOUR FIRST APP!

- Run your server