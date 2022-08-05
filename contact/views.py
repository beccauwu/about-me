from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, BadHeaderError
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

