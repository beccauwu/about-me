from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = f"{name.upper()} | {form.cleaned_data['subject']}"
			email = form.cleaned_data['email_address']
			message = form.cleaned_data['message']
			ebreak = '--------------------------------'
			greeting = f"Hello {name}!\n"
			content = "Your inquiry has been received and I'll get back to you as soon as possible!"
			signature = 'Best,\nRebecca Perttula'
			body = {
			'greeting': greeting,
			'content': content,
			'br1': ebreak,
			'message': f"Your inquiry:\n{message}",
			'signature': signature,
			}
			message = "\n".join(body.values())
			try:
				send_mail(subject, message, 'rebecca@perttula.co', ['rebecca@perttula.co'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
	form = ContactForm()
	return render(request, "contact.html", {'form':form})
