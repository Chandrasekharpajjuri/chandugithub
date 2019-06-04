from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .models import Curdmodel1,EmailSendModel,FormSetModel
from .forms import CurdForm,EmailSendForm,FormSetForm
from django.core.exceptions import ValidationError
from django.core import validators

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy


# def handle_uploaded_file(f):  
#         with open('cbvs_mongo_app/static/upload/'+f.name, 'wb+') as destination:  
#             for chunk in f.chunks():  
#                 destination.write(chunk)  

def Registration(request):
   #aved = False
   form=CurdForm()
   if request.method == "POST":
      #Get the posted form
      form = CurdForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         form=CurdForm()
         return render(request,"cbvs_mongo_app/curdmodel1_form.html",{'form':form,})#"msg":"upload sucessfully"})
   else:
      form=CurdForm()
      msg="file upload successfully"
      return render(request,"cbvs_mongo_app/curdmodel1_form.html",{'form':form,'mag':msg})

def Email_Send_View(request):
    form=EmailSendForm()
    if request.method == 'POST':
        form = EmailSendForm(request.POST,request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['File']) 
            From=request.POST.get('From','')
            To=request.POST.get('To','')
            Sub=request.POST.get('sub','')
            Message=request.POST.get('Message','')
            File_Attach=request.POST.get('Attach','')
           
            try:
                send_mail(Sub,Message,File_Attach,From,(To,))
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('sent')
            form.save()
            form=EmailSendForm()
            return render(request,'cbvs_mongo_app/emailsendform.html',{'form':form})
    else:
        form = EmailSendForm()
        return render(request,'cbvs_mongo_app/emailsendform.html',{'form':form})


class CurdListView(ListView):
    model=Curdmodel1

class CurdDetailView(DetailView):
    model=Curdmodel1


class CurdCreateView(CreateView):
    model=Curdmodel1
    fields='__all__'
    Template_name='cbvs_mongo_upload/Curdmodel1_form.html'
  
class CurdDeleteView(DeleteView):
    model=Curdmodel1
    success_url=reverse_lazy('Emp')
    

class CurdUpdateView(UpdateView):
    model=Curdmodel1
    fields='__all__'
    #list_display=('Select','Ename','Subject','Sal','Date_of_birth','Gender','Distric','Technologies','Search','File','User_Image','Passed')
    Template_name='cbvs_mongo_upload/Curdmodel1_form.html'

def cookies_count_view(request):
    c=int(request.COOKIES.get('c',0))
    newcount=c+1
    response=render(request,'cbvs_mongo_app/cookie.html',{'count':newcount})
    response.set_cookie('c',newcount,max_age=22)
    return response

def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    print(request.session.get_expire_age())
    print(request.session.get_expire_date())
    return render(request,'cbvs_momgo_app/page_count.html',{'count':newcount})



from django.forms import formsets as f
from django.http import HttpResponse

def FormSet_BookListView(request):
    ArticleFormSet=f.formset_factory(FormSetForm, extra=2, max_num=2)
    formset=ArticleFormSet()
    for i in formset:
        a=i.as_p()
        return HttpResponse(a)

#at terminal
#>>>formset=ArticleFormSet()
#>>>    for i in formset:
#>>>        a=i.as_p()
#>>>        print(i.as_table())

####creation for faker data and fake_mobile number






from faker import Faker
from random import *
#from random import randint
f=Faker()
def fake_data_retrive(request):
    f=Faker()
    n=int(input("How many names do you want:"))
    return render(request,'faker.html',{'f':f,'n':n})






def fake_data(views):
    n=int(input("How many names do you want:"))
    for i in range(1,n+1):
        print(f.name())
        print(f.city())
        print(f.email())
        print(f.address())
        n=''+str(randint(7,9))
        for i in range(0,9):
            n=n+str(randint(0,9))
        print(n)
        print(f.phone_number())
        print()


from random import *

def fake_phone(views):
    p=int(input("Enter how many no do you want:"))
    for i in range(p):
        d=randint(7,9)
        n=''+str(d)
        for i in range(9):
            n=n+str(randint(0,9))
        print(n)
        print()
		
    