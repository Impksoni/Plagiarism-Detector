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

def signup(request):
    return render(request, 'signup.html')

def aboutus(request):
    return render(request, 'aboutUs.html')

def contact(request):
    return render(request, 'contact.html')



r={}
def send_file(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.get("uploadfiles")
        myuploadfile(fName=name, myFile=myfile).save()
        
        queryset = myuploadfile.objects.all()
        #print(queryset)
        file=[]
        name=[]
        for obj in queryset:
            name.append(obj.fName)
            file.append(str(obj.myFile).lower())

        file.sort()
        name.sort()

        r=main(myfile)
        #print(data_queryset)
        plag=[]
        for i in range(len(r)):
            plag.append(r["data"+str(i)]["value"])

        #print(plag)

        data_queryset={}
        for i in range(len(queryset)):
            data_queryset["data"+str(i)]={"name":name[i],"file":file[i],"value":plag[i]}

        #print(data_queryset)

        res=dict(sorted(data_queryset.items(),key = lambda x: x[1]['value'], reverse=True))
        print(res)
        
        data={
            "data_list" : res
        }


        return render(request, 'result.html', data)

#        return HttpResponse("Uploaded!!")


#    return HttpResponse("Hello, world. You're at the  UI.")