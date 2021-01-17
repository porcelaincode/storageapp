from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account for {username} is created successfully!")
            return redirect('login-page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', { 'form': form })
