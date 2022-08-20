from django import forms
from .models import BlogPost
  
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('blogname', 'slug', 'blogauth', 'blogdes', 'blogcontent')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blogname'].widget.attrs.update({'class': 'form-control', 'id': 'titleInput'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control', 'id': 'slugInput'})
        self.fields['blogdes'].widget.attrs.update({'class': 'form-control', 'id': 'desInput'})
        self.fields['blogcontent'].widget.attrs.update({'class': 'form-control', 'id': 'contentInput'})