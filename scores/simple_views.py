from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def simple_login(request):
    """Minimal login view to bypass all potential issues"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # Direct authentication without form validation
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('simple_dashboard')
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'scores/simple_login.html')


@login_required
def simple_dashboard(request):
    """Minimal dashboard to avoid potential issues"""
    return render(request, 'scores/simple_dashboard.html')
