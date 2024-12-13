from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo']
        labels = {'photo':''}

    # photo = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))   