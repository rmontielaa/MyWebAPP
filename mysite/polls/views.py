import json
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
import json
from django.views.generic import ListView
from django.template import loader
from django.urls import reverse
from flask import Flask, render_template, abort, session
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
from .models import Question, choice

# Create your views here.

'''def index(request):
    questions =Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
'''
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['mensaje']="Lista de ecuestas"
        return context
    
    
    def get_queryset(self):
        query= Question.objects.order_by('-pub_date')[:5]
        return query
    
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))