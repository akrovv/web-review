from django.contrib import admin

from .models import AgeCategory, Genre, Game, Developer, Review

admin.site.register(AgeCategory)
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Review)