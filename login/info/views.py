from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from .forms import Userform
from .models import User
# Create your views here.
def myview(request):
    today=5+4
    return render(request,'hello.html',{"x":today})

def article(request,id):
    return HttpResponse("Dispalying article :%s"%id)

def login(request):
    if request.method == 'POST':

       form=Userform(request.POST)
       if form.is_valid():
           username=request.POST.get('username','')
           password=request.POST.get('password','')

       user_obj=User(username=username,password=password)
       user_obj.save()
       return render(request,'registration/login.html',{'form':form})

    else:
        form=Userform()
        return render(request,'registration/login.html',{'form':form})


def showdata(request):
     all_users=User.objects.all()
     return render(request,'main_page.html',{'all_users':all_users})



def main_page(request):
    template=get_template('main_page.html')
    variable=Context({'user':request.user})
    output=template.render(variable)
    return render(request,'main_page.html',{"username":"abhinav"})
