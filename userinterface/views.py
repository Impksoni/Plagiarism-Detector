from django.shortcuts import render
from django.http import HttpResponse

from . models import myuploadfile
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def send_file(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.get("uploadfiles")
        myuploadfile(fName=name, myFile=myfile).save()

        return HttpResponse("Uploaded!!")


#    return HttpResponse("Hello, world. You're at the  UI.")