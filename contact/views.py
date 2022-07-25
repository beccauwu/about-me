from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'rebecca@perttula.co', ['rebecca@perttula.co']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})
