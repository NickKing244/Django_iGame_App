from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/create', views.create_user),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('users/update', views.update_account),
    path('games/dashboard', views.all_games),
    path('games/:game_id/details', views.render_game_details),
    path('games/:game_id/unfavroite', views.unfavorite_game),
    path('games/search', views.render_search_page),
    path('users/account', views.render_account_page),
    path('games/find_game', views.search_games),
    path('games/favorite', views.favorite_game),
    path('games/add_note', views.add_note),

]