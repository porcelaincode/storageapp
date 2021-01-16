from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account for {username} is created successfully!")
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', { 'form': form })

def login(request):
    return render(request, 'users/login.html', {})