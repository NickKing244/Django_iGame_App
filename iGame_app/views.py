from django.shortcuts import render, HttpResponse, redirect

# Login/Resgister

def index(request):
    return render(request, 'index.html')

def create_user(request):
    pass

def login(request):
    pass

# Dashboard

def all_games(request):
    pass

def unfavorite_game(request):
    pass

def render_game_details(request):
    pass

def render_search_page(request):
    pass

def render_account_page(request):
    pass

# Search Page

def search_games(request):
    pass

def favorite_game(request):
    pass

# Details Page

def add_note(request):
    pass

# Account Page

def update_account(request):
    pass

def logout(request):
    pass