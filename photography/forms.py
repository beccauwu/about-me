from django import forms
from dal import autocomplete
from django.urls import reverse_lazy
from about_me.widgets import CustomAddAnotherWidgetWrapper
from .models import Image, Comment, Collection

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'id': 'titleEdit'})

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'img', 'collection')
        # widgets = {
        #     'collection': CustomAddAnotherWidgetWrapper(
        #         widget=forms.ModelChoiceField(queryset=Collection.objects.all()),
        #         add_related_url=reverse_lazy('collection-create'),
        #     )
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'id': 'titleInput'})
        self.fields['img'].widget.attrs.update({'class': 'form-control', 'id': 'imageInput'})

class CollectionCreateForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('name', 'summary')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'id': 'nameInput'}),
            'summary': forms.Textarea(attrs={'class': 'form-control mb-2', 'id': 'summaryInput'}),
        }

class CommentUploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows':1, 'cols':50, 'class': 'form-control mb-2', 'id': 'commentInput'}),
        }