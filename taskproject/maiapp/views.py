from django.shortcuts import render
from . models import Main
# Create your views here.
def task_ten(request):
    return render(request, 'form.html')
def task_four(request):
    hee=Main.objects.all()
    return render(request, 'submit.html',{"result":hee})
