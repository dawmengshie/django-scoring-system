from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def minimal_login(request):
    """Minimal login view to isolate 500 error"""
    if request.method == 'POST':
        return render(request, 'scores/minimal_login.html')
    
    return render(request, 'scores/minimal_login.html')
