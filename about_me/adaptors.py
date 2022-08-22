from django import forms
from django.utils.html import format_html
from inlineedit.adaptors import BasicAdaptor
from markdown import markdown
from photography.models import Comment

class FormControl(BasicAdaptor):
    def form_field(self):
        f = self._field.formfield()
        f.widget = forms.TextInput(attrs={'class': 'form-control mt-2 text-center d-inline wi-fc'})
        return f
    def display_value(self):
        return format_html(self.db_value())

class TextArea(BasicAdaptor):
    def form_field(self):
        f = self._field.formfield()
        f.widget = forms.Textarea(attrs={'class': 'form-control mt-2 text-center d-inline wi-fc'})
        return f
    def display_value(self):
        return format_html(markdown(self.db_value()))
