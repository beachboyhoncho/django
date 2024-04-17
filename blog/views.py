from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import AddBookForm,LoginForm,SignUpForm
from .models import Book

# Create your views here.
def add(request):
    form = AddBookForm(request.POST or None)
    if request.user.is_authenticated:
         if request.method == 'POST':
             if form.is_valid():
                add_book = form.save()
                messages.success(request,"book created successfully")
                return redirect('about')
         return render(request,'add.html',{'form':form})
    else:
         messages.success(request,"Logged in successfully")
         return redirect('login')


def about(request):
    books = Book.objects.all()
    return render(request,'about.html',{'books':books})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect('about')
            else:
                return redirect('login')
    else:
       form=LoginForm()
    return render(request,'login.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        #display registration form
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)
    if form.is_valid():
        new_user = form.save()
        login(request,new_user)
        messages.success(request,"Account created successfully")
        return redirect('login')
    #display blank invalid form
    context = {'form':form}
    return render(request,'signup.html',{'form':form})

def book(request,pk):
    if request.user.is_authenticated:
        book_record=Book.objects.get(id=pk)
        return render(request,'book.html',{'book_record':book_record})
    else:
        return redirect('about')
    
#delete logic    
def delete_book(request,pk):
    if request.user.is_authenticated:
        delete_it=Book.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Book deleted")
        return redirect('about')
    else:
        messages.success(request,"You must be logged in")
        return redirect('login')
    

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Book.objects.get(id=pk)
		form = AddBookForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('about')
		return render(request, 'update.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('login')


