from django.shortcuts import render

# Create your views here.

# from .models import Question


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('home/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return render(request, 'pages/home.html')


