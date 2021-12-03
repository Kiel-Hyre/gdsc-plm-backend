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

## BACKEND-05-TRANSFER
- Just transfer DJANGO views to DRF Views
- Instead of HttpResponse, Response from drf library was used
- Instead of Forms , serializers was used

- Serializer can be used as
    - Initial Validator
    - Output of serialized object, which was necessary for output response

- DIY
 - Conversion to Model Serializer
 - Exploring create, update, save of serializer
 - api_view() of delete, post, put  **NOTE in my case it was a bug**

- We created another app to just had a comparison in the regular Django
- If you want to really do the conversion (which is super great if you do that),
  feel free to change it :) (on your end)


### TADA!

- Run your server