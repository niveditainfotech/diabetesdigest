from django import forms
from .import models

class AddReview(forms.ModelForm):
    class Meta:
        model=models.Reviews
        fields='__all__'


class UploadPost(forms.ModelForm):
    class Meta:
        model=models.Post
        fields='__all__'

class Linkform(forms.ModelForm):
    class Meta:
        model=models.Links
        fields='__all__'