import imp
from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import *

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')

def quiz(request):
    if request.method == "POST":
        return render(request, 'quiz/results.html')

    else:
        questions = Questions.objects.all
        return render(request, 'quiz/quiz.html',{'questions':questions})
