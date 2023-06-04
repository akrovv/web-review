from django.urls import path
from .views import index, age_categories, genres, developers, game, add_review, add_to_favorites

app_name = 'review'

urlpatterns = [
    path('', index, name='index'),
    path('age_categories/', age_categories, name='age_categories'),
    path('genres/', genres, name='genres'),
    path('developers/', developers, name='developers'),
    path('game/<int:id>/', game, name="game"),
    path('add_review/', add_review, name="add_review"),
    path('add_to_favorites/', add_to_favorites, name='add_to_favorites'),
]
