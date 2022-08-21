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

class NewComment(BasicAdaptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = kwargs['image']
    def form_field(self):
        f = self._field.formfield()
        f.widget = forms.TextInput(attrs={'class': 'form-control mt-2 text-center d-inline wi-fc'})
        return f
    def empty_message(self):
        return 'Hover here to add new {}'.format(self._field.verbose_name)
    def save(self, value):
        Comment.create(image=self.image, comment=value, author=self._user)