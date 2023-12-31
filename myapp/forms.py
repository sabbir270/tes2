from django.forms import forms
from .models import Player
from django.forms import ModelForm

class GroupForm(ModelForm):
    class Meta:
        model=Player
        fields='__all__'