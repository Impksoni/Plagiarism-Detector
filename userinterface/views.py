from __future__ import absolute_import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from program import main

from . models import myuploadfile, reviewcontact

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                print("Login successful")
                return redirect("/")
            else:
                print('Username or Password is Incorrect')
                messages.error(request, 'Roll Number or Password is Incorrect')
                return redirect("/login/")
        else:
            print('Fill out all fields')
            messages.error(request, 'Fill out all the fields')
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phoneNo=request.POST.get('phoneNo')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            print("Enter correct roll")
            messages.error(request, 'Account already created')
            return redirect("/signup/")
        elif User.objects.filter(email=email).exists():
            print("Email already exits")
            messages.error(request, 'Email already exits')
            return redirect("/signup/")
        else:        
            myuser = User.objects.create_user(username=username,first_name = firstname,last_name = lastname,password=password,email=email)
            myuser.save()
            print('Your account has been created successfull!!')
            return redirect('/login/')    
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def aboutus(request):
    return render(request, 'aboutUs.html')

def contact(request):
    if request.method == 'POST':
        first = request.POST.get('firstname')
        last = request.POST.get('lastname')
        description = request.POST.get('description')
        email = request.POST.get('email')
        reviewcontact(first=first,last=last,email=email,description=description).save()
        messages.success(request, 'Your review submitted successfully')
        return redirect('/contact/')
    else:
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
        string=""
        data_queryset={}
        for i in range(len(queryset)):
            if plag[i] >=99:
                dub= "Dublicated document submitted"
            elif plag[i]<=40:
                string="Submission successful"
            else:
                string="Submission failed!! Highly plagiarized"
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