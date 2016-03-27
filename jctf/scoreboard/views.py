from django.shortcuts import render, get_object_or_404

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

def submit(request, problem_id):
    p = get_object_or_404(Problem, pk=problem_id)
    flag = request.POST.get('flag')
    result = (p.flag == flag)
    return render(request, 'problem.html', {'p': p,  'result': result})