from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpResponse

from program import main

from . models import myuploadfile
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

    
r={}
def send_file(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.get("uploadfiles")
        myuploadfile(fName=name, myFile=myfile).save()
        
        r=main(myfile)
        print(r)
        data={
            "data_list" : r
        }
        return render(request, 'result.html', data)

#        return HttpResponse("Uploaded!!")


#    return HttpResponse("Hello, world. You're at the  UI.")