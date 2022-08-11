from django import forms
  
class GalleryForm(forms.Form):
    collection = forms.CharField(max_length=200, required=True)
    collection_summary = forms.CharField(max_length=200, required=False)
    title = forms.CharField(max_length=200, required=True)