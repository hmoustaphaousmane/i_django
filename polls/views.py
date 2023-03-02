from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    question = get_object_or_404 (Question, pk = question_id)
    try :
        selected_choice = question.choise_set.get (pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) :
        # Redisplay the question voting form
        return render (request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else :
        selected_choice.votes += 1
        selected_choice.save ()
        # Always return a HttpResponseRedirect  after successfully dealing
        # with POST data. This prevents data from beung posted twice if a
        # user hits Back button.
        return HttpResponseRedirect (reverse ("polls/results", args (question_id)))
