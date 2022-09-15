from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import File
from .forms import UploadForm
from .serializers import FileSerializer

def index(request):
    return HttpResponse('Hello there')

def myapi(request):
    data = File.objects.all()
    return render(request, 'myapi/myapi.html', {'files': data, 'form':UploadForm})

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
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect(myapi)

# API version

def files(request):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'file': serializer.data})

def home(request):
    return HttpResponse("Hello there")
