from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse


def basic_login(request):
    """Ultra-basic login that bypasses Django auth"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        try:
            # Direct database lookup
            user = User.objects.get(username=username)
            
            # Simple password check (for testing only)
            if password == 'sammy123' and username == 'sammy':
                login(request, user)
                return redirect('basic_dashboard')
            elif password == 'nicos123' and username == 'nicos':
                login(request, user)
                return redirect('basic_dashboard')
            elif password == 'jerome123' and username == 'Jerome':
                login(request, user)
                return redirect('basic_dashboard')
            elif password == 'adrian123' and username == 'Adrian':
                login(request, user)
                return redirect('basic_dashboard')
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "User not found")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    
    return render(request, 'scores/basic_login.html')


def basic_dashboard(request):
    """Ultra-basic dashboard"""
    if not request.user.is_authenticated:
        return redirect('basic_login')
    
    return render(request, 'scores/basic_dashboard.html')


def test_auth(request):
    """Test authentication system"""
    try:
        from django.contrib.auth import authenticate
        user_count = User.objects.count()
        return JsonResponse({
            'auth_works': True,
            'user_count': user_count,
            'users': list(User.objects.values_list('username', flat=True)[:5])
        })
    except Exception as e:
        return JsonResponse({
            'auth_works': False,
            'error': str(e)
        })
