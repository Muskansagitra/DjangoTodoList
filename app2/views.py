from django.shortcuts import render,redirect

from app2.models import TodoModel

# Create your views here.
def todoadd(request):
    add = TodoModel.objects.order_by('-id')
    return render(request,'home.html',{'add':add})

def home(request):
    if request.method == "POST":
        name=request.POST.get("name")
        subject=request.POST.get("subject")
        activity=request.POST.get("activity")
        TodoModel.objects.create(name=name,subject=subject,activity=activity) 
    return redirect('todoadd')

def complete(request,id):
    cp = TodoModel.objects.get(id=id)
    cp.complete=True
    cp.save()        
    return redirect('home')

def delete(request,id):
    cp=TodoModel.objects.get(id=id)
    cp.delete()
    return redirect(home)

