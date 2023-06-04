from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserLoginForm, UserForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import GamePassed, Users

def logout_view(request):
    logout(request)
    return redirect('review:index')

@login_required
def profile(request):
    user = get_object_or_404(Users, username=request.user.username)
    favorite_games = user.favorite_games.all()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            game_name = user_form.cleaned_data['game_name']
            hours_played = user_form.cleaned_data['hours_played']
            developer = user_form.cleaned_data['developer']

            game_passed = GamePassed.objects.create(game_name=game_name, hours_played=hours_played, developer=developer)
            user.games.add(game_passed)

            return redirect('loginer:profile')
    else:
        user_form = UserForm()

    return render(request, 'loginer/profile.html', {'user': user, 'user_form': user_form, 'favorite_games': favorite_games})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect(reverse('review:developers'))

    else:
        form = UserLoginForm()

    context = {'form': form}

    return render(request, 'loginer/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('loginer:login'))
    else:
        form = UserRegisterForm()

    context = {'form' : form}

    return render(request, 'loginer/register.html', context)
