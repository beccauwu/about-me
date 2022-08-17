from django import forms
from dal import autocomplete
from django.urls import reverse_lazy
from about_me.widgets import CustomAddAnotherWidgetWrapper
from .models import Image, Comment

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'img', 'collection')
        widgets = {
            'collection': CustomAddAnotherWidgetWrapper(
                widget=autocomplete.ModelSelect2(url='collection-autocomplete'),
                add_related_url=reverse_lazy('collection-create'),
                add_icon='fa fa-plus',
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['collection'].widget.attrs.update({'class': 'form-control', 'id': 'collectionInput'})

class CommentUploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows':1, 'cols':50})
        }