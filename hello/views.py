from django.shortcuts import render
from django.http import HttpResponse

# v1
def hello(request):
    return HttpResponse("Hello World")

# v2
# https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#django.shortcuts.render
# def hello(request):
    # return render(request, 'hello.html')

    # v3
    # return render(request, 'hello.html', {'name': 'THE AUTHOR OF THIS APP'})

    # v4
    # https://docs.djangoproject.com/en/3.2/ref/templates/builtins/
    # context = {
    #     'name': 'Miguel', # change the name
    #     'to_do': [
    #         'homework',
    #         'cleaning mugs',
    #         'study',
    #         'gdsc study jam',
    #     ]
    # }
    # return render(request, 'hello.html', context)