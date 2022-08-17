from django import forms
from .models import Image, Comment

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'img', 'collection')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['collection'].empty_label = "Select a collection"
        self.fields['collection'].queryset = Image.objects.values_list('collection', flat=True).distinct()

class CommentUploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows':1, 'cols':50})
        }