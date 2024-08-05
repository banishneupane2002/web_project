from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from .models import UserForm

@login_required
def home(request):
    return render(request, "home.html", {})
def authview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:  
           return redirect("base:login")
 
        
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})

def user_form_view(request):
    return render(request, 'form.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        country = request.POST.get('country')
        message = request.POST.get('message')
        newsletter = request.POST.get('newsletter') == 'on'
        
        UserForm.objects.create(
            name=name,
            sex=sex,
            country=country,
            message=message,
            newsletter=newsletter
        )
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})