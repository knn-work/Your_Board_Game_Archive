from django.urls import path

from yboga.views import index, categories_view, category_detail, game_detail

urlpatterns = [
    path("", index),
    path("category/<slug:slug>/", category_detail, name="category_detail"),
    path("game/<slug:slug>/", game_detail, name="game_detail"),
    path("categories", categories_view, name="categories"),
]
