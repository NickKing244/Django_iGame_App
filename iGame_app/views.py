from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Login/Resgister

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == 'POST':
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], email=request.POST['email'], password=pw_hash)
            request.session['userid'] = User.objects.last().id
            print(request.session['userid'])
            return redirect('/games/dashboard')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            request.session['userid'] = user.id
            print(request.session['userid'])
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                return redirect('/games/dashboard')
        messages.error(request, "Email or password are not correct")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

# Dashboard

def all_games(request):
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'all_games': Game.objects.all(),
    }
    if 'userid' not in request.session:
        return redirect('/')
    else:
        return render(request, 'dashboard.html', context)

def unfavorite_game(request, game_id):
    if 'userid' not in request.session and request.method == 'POST':
        return redirect('/')
    else:
        this_game = Game.objects.get(id=game_id)
        this_game.delete()
    return redirect('/games/dashboard')

def render_game_details(request, game_id):
    context = {
        'game': Game.objects.get(id=game_id)
    }
    return render(request, 'details.html', context)

def render_account_page(request):
    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    if 'userid' not in request.session:
        return redirect('/')
    else:
        return render(request, 'account.html', context)

def render_add_game(request):
    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    if 'userid' not in request.session:
        return redirect("/")
    else:
        return render(request, 'add_game.html', context)

# Add Game Page

def create_game(request):
    this_user = User.objects.get(id=request.session['userid'])
    errors = Game.objects.game_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/games/new')
    else:
        Game.objects.create(title=request.POST['title'], developer=request.POST['developer'], publisher=request.POST['publisher'], genre=request.POST['genre'], summary=request.POST['summary'], release_date=request.POST['release_date'], platform=request.POST['platform'])
        return redirect('/games/dashboard')

# Account Page

def update_account(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/account')
    if 'userid' not in request.session:
        return redirect('/')
    else:
        this_user = User.objects.get(id=request.session['userid'])
        this_user.first_name = request.POST['first_name']
        this_user.last_name = request.POST['last_name']
        this_user.email = request.POST['email']
        this_user.save()
        return redirect('/users/account')