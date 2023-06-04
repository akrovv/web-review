from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

from .models import Game, AgeCategory, Genre, Developer, Review

from .forms import ReviewForm

def index(request):
    game_list = Game.objects.all()
    context = {
        'games': game_list
    }

    return render(request, 'review/index.html', context=context)

def age_categories(request):
    age_list = AgeCategory.objects.all()
    game_list = Game.objects.all()

    selected_age = request.GET.getlist('age')
    if selected_age and 'all' not in selected_age:
        game_list = game_list.filter(age__age__in=selected_age)

    context = {
        'age_list': age_list,
        'games': game_list,
        'selected_age': selected_age
    }

    return render(request, 'review/age_categories.html', context=context)


def genres(request):
    genres_list = Genre.objects.all()
    game_list = Game.objects.all()
    selected_genres = request.GET.getlist('genre')

    if selected_genres:
        genres = Genre.objects.filter(genre_name__in=selected_genres)
        game_list = Game.objects.filter(genre__in=genres)

    context = {
        'genres': genres_list,
        'games': game_list,
        'selected_genres': selected_genres,
    }

    return render(request, 'review/genres.html', context=context)

def developers(request):
    developer_list = Developer.objects.all()
    game_list = Game.objects.all()

    selected_developers = request.GET.getlist('developer')
    if selected_developers:
        game_list = game_list.filter(developer__developer_name__in=selected_developers)

    context = {
        'developers': developer_list,
        'games': game_list,
        'selected_developers': selected_developers
    }

    return render(request, 'review/developers.html', context=context)


def game(request, id):
    game_info = Game.objects.get(pk=id)
    reviews = game_info.reviews.all()

    return render(request, 'review/game.html', context={'game' : game_info, 'id': id, 'reviews' : reviews})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rating = form.cleaned_data['rating']
            review = form.cleaned_data['review']
            url_game = form.cleaned_data['url_game']

            game = Game.objects.get(pk=url_game)

            review = Review(name=name, rate=rating, full_review=review)
            review.save()

            review.games.add(game)

        return redirect('review:game', id=url_game)

    return redirect('review:index')

@login_required
def add_to_favorites(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        if game_id:
            game = get_object_or_404(Game, id=game_id)
            request.user.favorite_games.add(game)
            return redirect('review:game', id=game_id)

    return HttpResponseBadRequest()