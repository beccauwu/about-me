from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from about_me import views
# Create your views here.

def html_message(name, message):
    body = f"""
		<div style='text-align: center; border: 2px solid black; border-radius: 15px; width: 80%; margin: 0 auto; padding: 40px;'>
		<h3>Hi {name}!</h3>
		<p>I've received your inquiry and will get back to you as soon as possible.</p>
		<div style='padding-top:10px;border-top:2px solid black;width:80%;margin:40px auto 15px auto'></div>
		<div style='border: 2px solid black; border-radius: 15px;'>
		<div style='border-bottom: 2px solid black; width: 70%; margin: 40px auto;'>
		<p>Your message:</p>
		</div>
		<div style='padding: 5px 10px; border-left: 4px solid #d0d0d0; width:180px; margin: 0 auto;'>
		<p><em>{message}</em></p>
		</div>
		<div style='border-top: 2px solid black; width: 80%; margin: 40px auto;'></div>
		</div>
		<div style='margin: 5px auto;'></div>
		<p>In the meantime if you have anything else you would like to add, feel free to reply to this message instead of submitting a new inquiry.</p>
		<div style='padding-top:10px;border-top:2px solid black;width:80%;margin:40px auto 0 auto'>
		<h4>Best,</h4>
		<p>Rebecca Perttula</p>
		<p><a href='mailto:rebecca@perttula.co'>rebecca@perttula.co</a></p>
		<p><a href='tel:+46724416869'>+46724416869</a></p>
		</div>
		</div>
    """
    return body

def text_message(name, message):
    body = f"""
		Hi {name}!\n
  		I've received your inquiry and will get back to you as soon as possible.\n
    	Your message:\n
     	{message}\n
		In the meantime if you have anything else you would like to add, 
  		feel free to reply to this message instead of submitting a new inquiry.\n
     	Best,\n
      	Rebecca Perttula\n
		rebecca@perttula.co\n
		+46724416869
    """
    return body

@csrf_exempt
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = f"{name.upper()} | {form.cleaned_data['subject']}"
			to_email = form.cleaned_data['email_address']
			message = form.cleaned_data['message']
			return request.post(
				"https://api.eu.mailgun.net/v3/mail.perttula.co/messages",
				auth=("api", config("MAILGUN_API_KEY")),
				data={"from": "Rebecca Perttula <noreply@mail.perttula.co>",
					"to": f"{name} <{to_email}>",
					"subject": subject,
					"template": "contact",
					"h:X-Mailgun-Variables": f"{'name': 'name', 'message': {message}}"}),
			# try:
			# 	send_mail(
        	# 		subject=subject,
           	# 		message=text_content,
            #   		from_email='noreply@perttula.co',
            #     	recipient_list=['inbox@perttula.co', to_email],
            #      	html_message=html_content,
            #     )
			# except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			# return redirect ("home")
	form = ContactForm()
	return render(request, "contact.html", {'form':form})


