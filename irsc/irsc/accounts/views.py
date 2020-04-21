from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import(
    authenticate,
    get_user_model,
)
from .forms import UserLoginForm,UserRegisterForm

@login_required(login_url='accounts:login')
def home(request):
    return render(request,'accounts/home.html')


def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        auth_login(request,user)
        return redirect("user/")
    return render(request,'accounts/logIn.html',{"form":form})

# def register(request):
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=username,password=password)
#         auth_login(request,new_user)
#         return redirect("user/")
#     else:
#         return HttpResponse("not valid")
#     return render(request,'accounts/register.html',{"form":form})
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            print(form.cleaned_data.get("first_name"))
            auth_login(request, user)
            return redirect('/accounts/user/')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
