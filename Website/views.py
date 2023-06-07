from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm


def home(request):
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
       return render(request, 'home.html', {})


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