from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout, login, authenticate

# from django.contrib.auth.models import User
# Create your views here.


def signup_page(request):
    signup_form =UserCreationForm()
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)

        if signup_form.is_valid():
            user = signup_form.save()
            login(request,user)
            return redirect('blog_index')
    else:
        signup_form =UserCreationForm()
    
    return render(request,'account_signup.html',{'signup':signup_form})



def login_page(request):
    login_form = AuthenticationForm()

    if request.method == "POST":

        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user =login_form.get_user()
            login(request,user)
            return redirect('blog_index') 
    else:
        login_form = AuthenticationForm()
    return render(request,'account_login.html',{'login':login_form})


def logout_btn(request):
    if request.method == "POST":
        logout(request)
        return redirect('landing_page')



