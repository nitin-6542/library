

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect ,get_object_or_404 ,get_list_or_404 
from .models import Books 
from django.views import View
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate ,login ,logout

from django.contrib import messages

def index(request):
    return render(request, "start.html")

def sign_up(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        check =User.objects.filter(username=username)
        print(len(check))

        if len(check)==0:
        
            myuser = User.objects.create_user(username,"abc@gmail.com",password)
        
            myuser.save()
            messages.success(request, " Signup Successfully")
            return redirect('home')
        else:
            messages.error(request, " user already present")
            return redirect('home')



    else:
        return HttpResponse("404 - Not found")
def sign_in(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("successful")
            messages.success(request,"Sign in successfully")
            return render(request,"index.html")
        else:
            messages.error(request,"Wrong Password or Username")
            print("failed")
            return redirect('home')
    return render(request,"index.html")
def sign_out(request):
    logout(request)
    return redirect('home')

        
   


class addbooks(View):
    def get(self,request):
        if request.user.is_authenticated:
             
            return render(request, 'index.html')

    def post(self,request):
        if request.user.is_authenticated:
            if request.method == "POST":
                title = request.POST.get('title')
                author = request.POST.get('author')
                isbn = request.POST.get('isbn')
                print(isbn)
                print(author)
                print(isbn)

                book = Books(title=title, author=author, isbn=isbn)
                data=Books.objects.filter(title=title)
                if len(data)==0:
                    book.save()
                    x={"info":"Book added Successfully"}
                    print(x)
                else:
                    x={"info":"Book already Present"}
                    print(x)
                
                return render(request,'index.html',x)
       
class SearchBooks(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            print("inside")
            title = request.GET.get('search')
            print(title)
            data = Books.objects.filter(title=title)
            print(type(data))
            return render(request, 'index.html', {"data": data})
        else:
            return render(request, 'start.html')
    
class removebooks(View):
    def get(self,request):
        if request.user.is_authenticated:
             
            return render(request, 'index.html')
    def post(self,request):
        if request.user.is_authenticated:
        

            if request.method=="POST":
                isbn = request.POST.get("isbn_remove")
                print(isbn)
                data=Books.objects.filter(isbn=isbn)
                
                if len(data)==0:
                    
                
                    x={"infoo":"Book Not found"}
                    print(x)
                else:
                    for i in data:
                        data.delete()
                    x={"infoo":"Book Deleted Successfully "}
                    print(x)
                
                return render(request,'index.html',x)
        else:
            return render(request, 'start.html')

        
        

  






