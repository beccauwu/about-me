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
            name = str(form.cleaned_data['name']).capitalize()
            subject = f"{name.upper()} | {form.cleaned_data['subject']}"
            email = form.cleaned_data['email_address']
            from_email = "noreply@perttula.co"
            cc_email = 'mail@perttula.co'
            msg = form.cleaned_data['message']
            try:
                message = EmailMessage(
					subject=subject,
					from_email=from_email,
					to=[email],
     				cc=[cc_email])
                message.template_id = "contact"
                message.merge_global_data = {
					'name': name,
					'message': msg,
				}
                message.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

