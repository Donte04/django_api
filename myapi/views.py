from django.http import HttpResponse, Http404
from django.shortcuts import render
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
    data = File.object.all()
    return render(request, 'myapi/myapi.html', {'files': data})

def file(request, file_id):
    #f = next((item for item in data if item['id'] == file_id), None) # where next() is a python generator
    f = File.object.get(pk=file_id)
    if f is not None:
        return render(request, 'myapi/list.html', {'file':f})
    else:
        #raise Http404("File does not exist")
        return render(request, '404.html')
