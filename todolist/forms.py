from django import forms
from todolist.models import Task
from django.forms import TextInput


class CreateNew(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Insert task title..'
                }),
            'description': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Insert task description..'
                })
        }
