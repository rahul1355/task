from django.shortcuts import render,redirect
from taskapp.models import tasklist
from taskapp.forms import taskListForm,editTaskForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = taskListForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("new task added")
    
    form = taskListForm()
    tasks = tasklist.objects.all()
    paginator = Paginator(tasks,5)
    page = request.GET.get('pg')
    tasks = paginator.get_page(page)
    return render(request,"index.html",{'tasks':tasks,'form':form})

def completed_tasks(request):
    tasks = tasklist.objects.all()
    return render(request,"task_completed.html",{'tasks':tasks})

def pending_tasks(request):
    tasks = tasklist.objects.all()
    return render(request,"pending_task.html",{'tasks':tasks})

def edit_task(request,pk):
    if request.method == 'POST':
        res = tasklist.objects.get(id=pk)
        form = editTaskForm(request.POST,instance=res)
        if form.is_valid():
            form.save()
            return redirect('index')
    res = tasklist.objects.get(id=pk)
    form = editTaskForm(instance=res)
    return render(request,"edittask.html",{'form':form})

def delete_task(request,pk):
    res = tasklist.objects.get(id=pk)
    res.delete()
    return redirect('index')