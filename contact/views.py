from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from about_me import views
# Create your views here.

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email_address']
            subject = f"{str(fname + ' ' + lname).upper()} | {form.cleaned_data['subject']}"
            from_email = 'mail@perttula.co'
            msg = form.cleaned_data['message']
            recipients = [[email, subject], ['mail@perttula.co' , f'New Message from {email}']]
            try:
                for recipient in recipients:
                    message = EmailMessage(
                        subject=recipient[1],
                        from_email=from_email,
                        to=[recipient[0]])
                    message.template_id = 'contact'
                    message.merge_global_data = {
                        'name': str(fname).capitalize(),
                        'message': msg,
                    }
                    message.esp_extra = {
                        'o:tag': 'resume contact form',
                    }
                    message.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

