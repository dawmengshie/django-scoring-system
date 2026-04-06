from django.urls import path
from . import views
from . import simple_views
from . import basic_views
from . import test_views
from . import minimal_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login_url'),
    path('minimal/', minimal_views.minimal_login, name='minimal_login'),
    path('test500/', test_views.test_view, name='test500'),
    path('basic/', basic_views.basic_login, name='basic_login'),
    path('simple/', simple_views.simple_login, name='simple_login'),
    path('debug/', views.debug_view, name='debug'),
    path('test-auth/', basic_views.test_auth, name='test_auth'),
    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('basic-dashboard/', basic_views.basic_dashboard, name='basic_dashboard'),
    path('simple-dashboard/', simple_views.simple_dashboard, name='simple_dashboard'),
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
