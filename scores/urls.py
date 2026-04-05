from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login_redirect'),
    path('debug/', views.debug_view, name='debug'),
    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    
    path('add/merit/', views.add_merit, name='add_merit'),
    path('add/demerit/', views.add_demerit, name='add_demerit'),
    
    path('team/<int:team_id>/', views.team_details, name='team_details'),
    
    # Team Color Management URLs
    path('manage/colors/', views.manage_colors, name='manage_colors'),
    path('manage/colors/add/', views.add_team_color, name='add_team_color'),
    path('manage/colors/<int:color_id>/edit/', views.edit_team_color, name='edit_team_color'),
    path('manage/colors/<int:color_id>/delete/', views.delete_team_color, name='delete_team_color'),
    path('manage/teams/<int:team_id>/edit/', views.edit_team, name='edit_team'),
    path('manage/teams/<int:team_id>/delete/', views.delete_team, name='delete_team'),
    path('manage/teams/<int:team_id>/reset/', views.reset_team_scores, name='reset_team_scores'),
]
