from django import forms
from dal import autocomplete
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper
from .models import Image, Comment

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'img', 'collection')
        widgets = {
            'collection': AddAnotherWidgetWrapper(
                autocomplete.ModelSelect2(url='collection-autocomplete'),
                reverse_lazy('collection-create')
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommentUploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows':1, 'cols':50})
        }