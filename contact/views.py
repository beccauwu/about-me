from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = f"{name.upper()} | {form.cleaned_data['subject']}"
			to_email = form.cleaned_data['email_address']
			message = form.cleaned_data['message']
			pstart = "<p style='text-align: center;'>"
			pend = "</p>"
			body = {
			'greeting': f"<h3 style='text-align: center;'>Hello {name},</h3>",
			'content': f'{pstart}I have received your inquiry and will respond as soon as possible.{pend}',
			'br1': '--------------------------------',
			'strong': f'{pstart}<strong>Your inquiry:</strong></p>{pend}',
			'divstart': "<div style='padding: 12px; border-left: 4px solid #d0d0d0; width: fit-content; margin: 0 auto;'>",
			'message': f"<p style='font-style: italic; text-align: center;'>{message}</p>",
			'divend': '</div>',
			'signature': 'Best,<br>Rebecca Perttula',
			}
			html_content = "<br>".join(body.values())
			text_content = f"Hi {name}!\nI've received your message and will get back to you asap:\nYour message:\n{message}\nBest,\nRebecca Perttula"
			try:
				send_mail(
        			subject=subject,
           			message=text_content,
              		from_email='noreply@perttula.co',
                	recipient_list=['inbox@perttula.co', to_email],
                 	html_message=html_content
                )
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
	form = ContactForm()
	return render(request, "contact.html", {'form':form})
