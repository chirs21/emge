from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm ,UserRegistrationForm
from accounts.forms import UserForm
from accounts.forms import forgotForm
from Magenta.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

def index(request):
    #Return the index html file
    return render(request, 'home/home.html')

def fp(request):
    sub = forgotForm()
    if request.method == 'POST':
        sub = forgotForm(request.POST)
        subject = 'Forgot Password'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'home/success.html', {'recepient': recepient})
    return render(request,'accounts/fp.html',{'form':sub})

#@login_required


def cp(request):
    return render(request,'accounts/cp.html')

"""    
def logout(request):
    #Log the user out
    auth.logout(request)
    messages.success(request, "You have successfuly been logged out")
    return redirect(reverse('login'))
def login(request):
    # Return a login page
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
                                     
            
            if user:
                auth.login(user=user, request=request)
                
                messages.success(request, "You have successfuly logged in!")
                return redirect(reverse('home'))
                
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'accounts/login.html', {"login_form": login_form})


def register(request):
    # Render the registration page
    return render(request,'accounts/register.html')
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account at this time")
            
    else:
        registration_form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', { 
        "registration_form": registration_form})

"""

def organisation(request):

    if request.method == 'POST':
        form1 = UserForm(request.POST, request.FILES or None)
        print(form1.errors)

        if form1.is_valid():
            form1.save()
            return redirect('home')
    else:
        form1 = UserForm()
        
    context = {'form1' : form1}
    return render(request,'accounts/organisation.html',context)
    