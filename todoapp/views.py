from django.urls import reverse_lazy
from . models import Task
from django.shortcuts import render, redirect
from . forms import TodoForm

from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.

class TaskListView(ListView):
    model=Task
    template='index.html'
    context_text_name='var2'

class TaskDetailView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task1'
    fields=('name','priority','date')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url =reverse_lazy('cbvhome')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
def add(request):
    var2 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        var1=Task(name=name,priority=priority,date=date)
        var1.save()

    return render(request,'index.html',{'var2':var2})

# def detail(request):
#     var2=Task.objects.all()
#     return render(request,'detail.html',{'var2':var2})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html', {'f': f, 'task': task})