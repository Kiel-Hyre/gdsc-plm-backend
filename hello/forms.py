from django import forms


class ActionAddForm(forms.Form):
    text = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)


class ActionUpdateForm(ActionAddForm):
    pass



# modelForm
from . import models

class ActionAddModelForm(forms.ModelForm):
    # text = forms.CharField(max_length=255)
    # description = forms.CharField(max_length=255)

    class Meta:
        model = models.Action
        fields = ['text', 'description'] # can be '__all__' if all were needed
        # exclude = [] if want some other but not the specified field in the exclude


class ActionUpdateModelForm(ActionAddModelForm):
    pass