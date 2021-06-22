from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm, UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.settings import EMAIL_HOST_USER
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail



# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            
            
            subject="Welcome"
            message="Congrats on registration"
            recepient=str(form['email'].value())
            send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request, 'subscribe/email.html', {'recepient': recepient})
        
            login(request, user)
            return redirect("dashboard")
        context={'form':form}
        
        return render(request, 'users/register.html', {'form':form})
            

@login_required

def delete_user(request):
    if request.method =='POST':
        delete_form=UserDeleteForm(request.POST, instance=request.user)
        user=request.user
        user.delete()
        messages.info(request,'Your account has beeen deleted')
        return redirect('dashboard')
    else: 
        delete_form=UserDeleteForm(instance=request.user)
        
    context={'delete_form': delete_form}
    return render(request,'users/delete_account.html',context)