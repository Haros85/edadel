from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new-recipe/', views.new_recipe, name='new_recipe'),
    path("follow/", views.follow_view, name="follow_view"),
    path('recipe/<slug>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<slug>/delete/', views.recipe_delete, name='recipe_delete'),
    path("profile/<username>/", views.profile, name='profile'),
    path('profile/<username>/recipe/<slug>/', views.recipe_view, name='recipe_view'),
    path("favorite/", views.favor_view, name="favor_view"),
    path('shop-list/', views.shop_list, name='shop-list'),
   # path('download', views.download, name='download'),
]
