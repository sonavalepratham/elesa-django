from django.shortcuts import render, HttpResponseRedirect,reverse,HttpResponse
from django.db import connection
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime,timedelta
from .models import extenduser
# Create your views here.
def index(request):
    return render(request,'login.html')

def HandleLogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('UpdateProfile'))

    if request.method=="POST":
        usrnm=request.POST['usrnm']
        passwrd= request.POST['pass']
        user= authenticate(username=usrnm,password=passwrd)
        if user is not None:  
            login(request,user)
            return HttpResponseRedirect(reverse('UpdateProfile'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

def HandleLogout(request):
    logout(request)
    return render(request,'login.html')

def viewboard(request):
    users = extenduser.objects.filter(board='Assistant')
    params={'users':users}
    return render(request,'card.html',params)

def UpdateProfile(request):
    if request.method=="POST":
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        board = request.POST['board']
        post = request.POST['post']
        pref_dict = {'PRESIDENT':0,'VICE PRESIDENT':1, 'SECRETARY':2, 'DIRECTOR OF FINANCE':3,'EVENT DIRECTOR':4,'CLUB SERVICE DIRECTOR':5, 'TECHNICAL DIRECTOR':6,'APTITUDE DEVELOPER':7,'ARO & PUBLICITY OFFICER':8,'DESIGNER':9,'WEB DEVELOPER':10}
        pref = pref_dict[request.POST['pref']]
        insta = request.POST['insta']
        git = request.POST['git']
        linkedin = request.POST['linkedin']
        img = request.POST['img']
        prev = extenduser.objects.filter(user_id=request.user.id)
        try:
            for i in prev:
                i.post=post
                i.board=board
                i.instagram=insta
                i.github=git
                i.linkedin=linkedin
                i.photo=uploaded_file_url
                i.post_pref=pref
                i.save()

        except:
            obj = extenduser(post=post, board=board, instagram=insta, github=git, linkedin=linkedin, photo=uploaded_file_url, post_pref=pref,user_id=request.user.id)
            obj.save()
    if request.user.is_authenticated:
        
        return render(request,'post_form.html')
    return HttpResponseRedirect(reverse('index'))

def Register(request):
    if request.method=="POST":
        usrnm=request.POST['usrnm']
        passwrd1= request.POST['pass1']
        passwrd2 = request.POST['pass2']
        email = request.POST['email']
        f_nm = request.POST['f_nm']
        email = request.POST['email']
        l_nm = request.POST['l_nm']
        if passwrd1==passwrd2:
            user = User.objects.create_user(username=usrnm, password=passwrd1, email=email, last_name=l_nm, first_name=f_nm)
            user.save()
            if user is not None:
                return HttpResponse('Account Created SuccessFully, Now You Can Login')
            else:
                return HttpResponse('Error') 
    return render(request,'registration.html')