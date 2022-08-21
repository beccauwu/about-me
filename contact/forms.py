from django.forms import CharField, TextInput, EmailField, Textarea, Form, ChoiceField, Select, EmailInput

# Create your forms here.

class ContactForm(Form):
    CHOISES = (
        ('Select subject', 'Select subject'),
        ('Request for quote on a job', 'Request for quote on a job'),
        ('Website inquiry', 'Website inquiry'),
        ('Other', 'Other'))
    subject = ChoiceField(choices=CHOISES, widget=Select(attrs={'class': "form-select giBold", 'id': 'subjectInput'}))
    fname = CharField(max_length = 50, required=True, widget=TextInput(attrs={'class': "form-control giBold nameInput", 'id': 'fnameInput', 'placeholder': 'Nathaneal'}))
    lname = CharField(max_length = 50, required=True, widget=TextInput(attrs={'class': "form-control giBold nameInput", 'id': 'lnameInput', 'placeholder': 'Down'}))
    email_address = EmailField(max_length = 150, required=True, widget=EmailInput(attrs={'class': "form-control giBold", 'id': 'emailInput', 'placeholder': 'name@example.com'}))
    message = CharField(max_length = 2000, required=True, widget=Textarea(attrs={'class': "form-control giBold", 'id': 'msgInput', 'placeholder': 'Message'}))
