from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import File

data = [
    {'id':0,
     'name':'file1.txt',
     'type':'txt'},
    {'id':1,
     'name':'file2.png',
     'type':'png'},
    {'id':2,
     'name':'file3.pdf',
     'type':'pdf'},
]

def index(request):
    return HttpResponse('Hello there')

def myapi(request):
    data = File.objects.all()
    return render(request, 'myapi/myapi.html', {'files': data})

def file(request, file_id):
    #f = next((item for item in data if item['id'] == file_id), None) # where next() is a python generator
    f = File.objects.get(pk=file_id)
    if f is not None:
        return render(request, 'myapi/file.html', {'file':f})
    else:
        #raise Http404("File does not exist")
        return render(request, '404.html')

def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id)
    print(name, file_type, f)

    if f:
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        f.save()
        return redirect(myapi)
    else:
        return redirect(myapi)

def delete(request, file_id):
    f = File.objects.get(pk=file_id)
    if f:
        f.delete()
    return redirect(myapi)

def upload(request):
    file = request.POST.get('file')
    if file:
        file.save()
    return redirect(myapi)
