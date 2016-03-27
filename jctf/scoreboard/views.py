from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Problem

def index(request):
    #return HttpResponse("Hello world")
    try:
      ps = Problem.objects.all()
    except e:
     pass
    return render(request, 'board.html', {'data': ps})

def problem(request, problem_id):
    p = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'problem.html', {'p': p})

