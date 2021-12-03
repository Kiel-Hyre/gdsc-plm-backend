from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from . import models # v5
from . import forms # 6

# v1
# def hello(request):
#     return HttpResponse("Hello World")

# v2
# https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#django.shortcuts.render
def hello(request):
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

    # v5 cont
    # context = {
    #     'name': 'Miguel',
    #     'to_do': models.Action.objects.all(),
    #     # 'to_do': models.Action.objects.all().values_list('text', flat=True),
    # }
    # return render(request, 'hello.html', context)

    # v6
    # by default once the page was loaded it tries a GET METHOD
    if request.method == 'GET':
        # raise Exception(True)

        context = {
            'name': 'Miguel',
            'to_do': models.Action.objects.all(),
            # 'to_do': models.Action.objects.all().values_list('text', flat=True),
        }
        return render(request, 'hello.html', context)

def hello_view(request, pk):
    if request.method == 'GET':
        obj = get_object_or_404(models.Action, pk=pk)
        return render(request, 'hello-view.html', {'data': obj})
    return HttpResponseRedirect(reverse('hello-index'))

def hello_delete(request, pk):
    obj = get_object_or_404(models.Action, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('hello-index'))
    return render(request, 'hello-delete.html', {'data': obj})


def hello_add(request):
    context = {}
    form = forms.ActionAddForm()

    if request.method == 'POST':

        # normal form
        form = forms.ActionAddForm(request.POST)
        if form.is_valid():
            models.Action.objects.create(**form.cleaned_data)

        # modelform
        # form = forms.ActionAddModelForm(request.POST)
        # if form.is_valid(): form.save()

        return HttpResponseRedirect(reverse('hello-index'))
    context['form'] = form
    return render(request, 'hello-add.html', context)


def hello_update(request, pk ):
    obj = get_object_or_404(models.Action, pk=pk)

    context = {}
    form = forms.ActionUpdateForm()

    # manually initialize all values from object to the form
    form.fields['text'].initial = obj.text
    form.fields['description'].initial = obj.description

    if request.method == 'POST':
        # normal form
        form = forms.ActionUpdateForm(request.POST)
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                setattr(obj, k, v)
            obj.save()
        return HttpResponseRedirect(reverse('hello-index'))
    context['form'] = form
    context['data'] = obj

    # modelform version
    # context = {}
    # form = forms.ActionUpdateModelForm(instance=obj)
    # if request.method == 'POST':
        # form = forms.ActionUpdateModelForm(request.POST, instance=obj)
        # if form.is_valid(): form.save()

    return render(request, 'hello-update.html', context)
