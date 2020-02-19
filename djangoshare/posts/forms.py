from django import forms

class PostUpdateForm(forms.ModelForm):
    image = forms.ImageField()