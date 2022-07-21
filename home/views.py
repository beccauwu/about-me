from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# from .models import Question


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('home/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return render(request, 'pages/home.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request=request, template_name='registration/login.html', context={'login_form':form})
