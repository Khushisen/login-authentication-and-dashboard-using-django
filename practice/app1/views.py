from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                form.add_error(None,"invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

@login_required
def dashboard_view(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

