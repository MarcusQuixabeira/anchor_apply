from django.forms import ModelForm
from .models import Avaliation

class AvaliationForm(ModelForm):
    class Meta:
        model = Avaliation
        fields = ['upload']
