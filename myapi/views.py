from django.http import HttpResponse, Http404, JsonResponse #JsonResponse for JSON format, HttpResponse for web template
from django.shortcuts import render, redirect
from .models import File
from .forms import UploadForm
from .serializers import FileSerializer
from rest_framework.response import Response #used like JsonResponse, but it allows to add status code information
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def file(request, file_id, format=None): #the third argument (format=None) is in order to apply "url suffix pattern"
    try:
        data = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(data)
    return Response({'file':serializer.data}, status=status.HTTP_200_OK)

def files(request):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'file': serializer.data})

def home(request):
    return HttpResponse("Hello there")


"""
Status codes:
def is_informational(code):
    return 100 <= code <= 199


def is_success(code):
    return 200 <= code <= 299


def is_redirect(code):
    return 300 <= code <= 399


def is_client_error(code):
    return 400 <= code <= 499


def is_server_error(code):
    return 500 <= code <= 599
"""
