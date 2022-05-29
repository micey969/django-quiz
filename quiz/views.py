import imp
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import *

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')

def quiz(request):
    questions = Questions.objects.all()
    if request.method == "POST":
        score = 0
        total = 0
        correct = 0
        incorrect = 0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            if q.answer == request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                incorrect+=1
        percentage = (score/ (total*10)) * 100
        context = {
            'score': score,
            'correct': correct,
            'incorrect': incorrect,
            'percentage': percentage
        }
        return render(request, 'quiz/results.html', context)

    else:
        return render(request, 'quiz/quiz.html',{'questions':questions})
