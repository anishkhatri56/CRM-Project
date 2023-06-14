from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()

    #for user logging check 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username = username, password = password )
        if user is not None: 
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an error in Logging Details, Please try again")
            return redirect('home')
    else:
       return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have Been logged out")
    return redirect('home')


3

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()    
            #for authentication after registrations
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =authenticate(username = username, password = password)
            login(request,user)
            messages.success(request, "You have sucessfully Registered, Welcome")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form} )
        
    return render(request, 'register.html',{'form':form} )


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
        return render(request, 'record.html',{'customer_record':customer_record} )
    else:
        messages.success(request, "You must be Logged In to acess this page.....")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk) 
        delete_it.delete()
        messages.success(request, "Record Deleted Sucessfully.....")
        return redirect('home')
    else: 
        messages.success(request, "Please create account to prompt this action.....")
        return redirect('home')


def add_record(request):
    return render (request, 'add_record.html', {})
