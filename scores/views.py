from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Sum, F
from django.http import JsonResponse
from django.conf import settings
from .models import Team, ScoreEntry, TeamColor
from .forms import ScoreEntryForm, TeamColorForm, TeamForm


def debug_view(request):
    """Debug view to check system status"""
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "OK"
    except Exception as e:
        db_status = f"Error: {str(e)}"
    
    try:
        from django.contrib.auth.models import User
        user_count = User.objects.count()
        
        # Check specific users
        staff_users = ['sammy', 'nicos', 'Jerome', 'Adrian', 'admin']
        user_status = {}
        for username in staff_users:
            try:
                user = User.objects.get(username=username)
                user_status[username] = {
                    'exists': True,
                    'is_staff': user.is_staff,
                    'is_active': user.is_active,
                    'is_superuser': user.is_superuser
                }
            except User.DoesNotExist:
                user_status[username] = {'exists': False}
    except Exception as e:
        user_count = f"Error: {str(e)}"
        user_status = {}
    
    return JsonResponse({
        'status': 'debug_info',
        'database': db_status,
        'user_count': user_count,
        'user_status': user_status,
        'debug_mode': settings.DEBUG,
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'database_config': {
            'engine': settings.DATABASES['default']['ENGINE'],
            'name': str(settings.DATABASES['default']['NAME'])
        }
    })


def login_view(request):
    if request.method == 'POST':
        try:
            from django.contrib.auth import authenticate, login
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '')
            
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('dashboard')
        except Exception as e:
            pass
    
    from django.contrib.auth.forms import AuthenticationForm
    return render(request, 'scores/simple_login_standalone.html', {'form': AuthenticationForm()})


@login_required
def dashboard(request):
    teams = Team.objects.annotate(
        total_score=Sum('score_entries__points')
    ).order_by('-total_score')
    
    recent_entries = ScoreEntry.objects.select_related('team', 'recorded_by').order_by('-date')[:10]
    
    context = {
        'teams': teams,
        'recent_entries': recent_entries,
    }
    return render(request, 'scores/dashboard.html', context)


@login_required
def scoreboard(request):
    teams = Team.objects.annotate(
        total_score=Sum('score_entries__points')
    ).order_by('-total_score')
    
    context = {'teams': teams}
    return render(request, 'scores/scoreboard.html', context)


@login_required
def add_merit(request):
    return add_score(request, 'merit')


@login_required
def add_demerit(request):
    return add_score(request, 'demerit')


def add_score(request, score_type):
    if request.method == 'POST':
        form = ScoreEntryForm(request.POST)
        if form.is_valid():
            score_entry = form.save(commit=False)
            score_entry.score_type = score_type
            score_entry.recorded_by = request.user
            
            # Set points based on score type if not specified
            if score_type == 'merit':
                score_entry.points = abs(score_entry.points)
            else:
                score_entry.points = -abs(score_entry.points)
            
            score_entry.save()
            messages.success(request, f"{score_type.title()} added successfully!")
            return redirect('dashboard')
    else:
        form = ScoreEntryForm()
    
    context = {
        'form': form,
        'score_type': score_type,
        'title': f'Add {score_type.title()}'
    }
    return render(request, 'scores/add_score.html', context)


@login_required
def team_details(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    entries = team.score_entries.select_related('recorded_by').order_by('-date')
    
    context = {
        'team': team,
        'entries': entries,
    }
    return render(request, 'scores/team_details.html', context)


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('login')
    else:
        return redirect('dashboard')


@login_required
def manage_colors(request):
    team_colors = TeamColor.objects.all()
    teams = Team.objects.select_related('color').all()
    return render(request, 'scores/manage_colors.html', {
        'team_colors': team_colors,
        'teams': teams
    })


@login_required
def add_team_color(request):
    if request.method == 'POST':
        form = TeamColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Team color "{form.cleaned_data["name"]}" has been added successfully!')
            return redirect('manage_colors')
    else:
        form = TeamColorForm()
    
    return render(request, 'scores/add_team_color.html', {'form': form})


@login_required
def edit_team_color(request, color_id):
    team_color = get_object_or_404(TeamColor, id=color_id)
    
    if request.method == 'POST':
        form = TeamColorForm(request.POST, instance=team_color)
        if form.is_valid():
            form.save()
            messages.success(request, f'Team color "{form.cleaned_data["name"]}" has been updated successfully!')
            return redirect('manage_colors')
    else:
        form = TeamColorForm(instance=team_color)
    
    return render(request, 'scores/edit_team_color.html', {
        'form': form,
        'team_color': team_color
    })


@login_required
def delete_team_color(request, color_id):
    team_color = get_object_or_404(TeamColor, id=color_id)
    
    # Check if any teams are using this color
    if team_color.teams.exists():
        messages.error(request, f'Cannot delete "{team_color.name}" - it is being used by teams.')
        return redirect('manage_colors')
    
    if request.method == 'POST':
        color_name = team_color.name
        team_color.delete()
        messages.success(request, f'Team color "{color_name}" has been deleted successfully!')
        return redirect('manage_colors')
    
    return render(request, 'scores/delete_team_color.html', {'team_color': team_color})


@login_required
def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, f'Team "{form.cleaned_data["name"]}" has been updated successfully!')
            return redirect('manage_colors')
    else:
        form = TeamForm(instance=team)
    
    return render(request, 'scores/edit_team.html', {
        'form': form,
        'team': team
    })


@login_required
def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == 'POST':
        team_name = team.name
        team.delete()
        messages.success(request, f'Team "{team_name}" has been deleted successfully!')
        return redirect('manage_colors')
    
    context = {
        'team': team,
        'title': 'Delete Team'
    }
    return render(request, 'scores/delete_team.html', context)


@login_required
def reset_team_scores(request, team_id):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to reset team scores.')
        return redirect('team_details', team_id=team_id)
    
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == 'POST':
        # Delete all score entries for this team
        deleted_count = team.score_entries.count()
        team.score_entries.all().delete()
        messages.success(request, f'All scores for "{team.name}" have been reset. {deleted_count} entries were deleted.')
        return redirect('team_details', team_id=team_id)
    
    context = {
        'team': team,
        'title': f'Reset {team.name} Scores'
    }
    return render(request, 'scores/reset_team_scores.html', context)
