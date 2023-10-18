from django.shortcuts import render

# Create your views here.
def task(request):
    return render(request,'task.html')

def task_one(request):
    return render(request,'Login.html')

def task_two(request):
    return render(request,'register.html')

def task_six(request):
    return render(request,'form.html')


