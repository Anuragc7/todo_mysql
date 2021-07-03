from django.shortcuts import render,redirect
from . models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class taskListview(ListView):
    model = task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class taskDetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'i'

class taskUpdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskDeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')


def task_view(request):
    obj1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,taskid):
    new=task.objects.get(id=taskid)
    if request.method == 'POST':
        new.delete()
        return redirect('/')
    return render(request,'delete.html',{'new':new})

def update(request,id):
    new1=task.objects.get(id=id)
    form=todoform(request.POST or None,instance=new1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'new1':new1,'form':form})