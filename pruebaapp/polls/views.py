from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import Question
# Create your views here.

def index(request):
  lastest_questions_list = Question.objects.all()
  return render(request, "polls/index.html", {
    "lastest_questions_list": lastest_questions_list
  })

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  print(question)
  return render(request, "polls/detail.html", {
    "question": question
  })

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return HttpResponse(question)

def votes(request, question_id):
  return HttpResponse(f"Estas votando a la pregunta número {question_id}")
