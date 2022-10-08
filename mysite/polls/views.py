import json
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
from django.template import loader

from .models import Question, choice

# Create your views here.

def index(request):
    questions =Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#'''def hola_dos(request):
 #   return HttpResponse("hola Mundo/2")'''

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context={
        'question' : question
    }
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)