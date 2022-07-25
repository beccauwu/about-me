from django.forms import CharField, TextInput, EmailField, Textarea, Form, ChoiceField, Select

# Create your forms here.

class ContactForm(Form):
    CHOISES = (
        ('Select subject', 'Select subject'),
        ('Request for quote on a job', 'Request for quote on a job'),
        ('Website inquiry', 'Website inquiry'),
        ('Other', 'Other'))
    subject = ChoiceField(choices=CHOISES, widget=Select(attrs={'class': "form-select", 'id': 'subjectInput'}))
    name = CharField(max_length = 100, required=True, widget=TextInput(attrs={'class': "form-control", 'id': 'nameInput', 'placeholder': 'Nathaneal Down'}))
    email_address = EmailField(max_length = 150, required=True, widget=TextInput(attrs={'class': "form-control", 'id': 'emailInput', 'placeholder': 'name@example.com'}))
    message = CharField(max_length = 2000, required=True, widget=Textarea(attrs={'class': "form-control", 'id': 'msgInput', 'placeholder': 'Message'}))
