from django.shortcuts import render
from django.http import Http404
# from django.template import loader
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by ('-pub_date') [:5]
    context = {'latest_questions' : latest_questions,}
    return render (request, 'polls/index.html', context)

def detail (request, question_id) :
    try :
        question = Question.objects.get (pk = question_id)
    except Question.DoesNotExist :
        raise Http404 ("Question does not exist.")
    # Shortcut : question = get_object_or_404(Question, pk=question_id)
    return render (request, 'polls/detail.html', {'question' : question})

def results (request, question_id) :
    response = "You are looking at the results of question %s."
    return HttpResponse (response % question_id)

def vote (request, question_id) :
    return HttpResponse("Your're voting on question %s" % question_id)
