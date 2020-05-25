from django import forms
from django.forms import ModelForm
from .models import Friend


class AddFriend(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta():
        model = Friend
        fields = '__all__'


