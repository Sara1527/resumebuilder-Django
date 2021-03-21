from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Resume
from .forms import ResumeForm,signinform
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="/signin/")
def home(request):
    resume = Resume.objects.all()
    p=Paginator(resume,3)
    try:
        page_number=request.GET.get('page')
        page_object=p.page(page_number)
    except:
        page_object = p.page(1)
    return render(request,'home.html',{'page_object':page_object})

@login_required(login_url="/signin/")
def forms(request):
    if request.method == "POST":
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ResumeForm()
    return render(request,'forms.html',{'form':form})

@login_required(login_url="/signin/")
def resumedetails(request,details=''):
    resume=Resume.objects.filter(name=details)
    return render(request,'resumedetails.html',{'resume':resume})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("User not found")
        else:
            login(request, user)
            return redirect('/')
    else:
        form = signinform()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/signin/')