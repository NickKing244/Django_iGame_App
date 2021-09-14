from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/create', views.create_user),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('users/update', views.update_account),
    path('games/dashboard', views.all_games),
    path('games/<int:game_id>/details', views.render_game_details),
    path('games/<int:game_id>/unfavorite', views.unfavorite_game),
    path('users/account', views.render_account_page),
    path('games/create', views.create_game),
    path('games/new', views.render_add_game),
]