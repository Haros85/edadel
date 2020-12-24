from django.urls import path

from . import views


urlpatterns = [
     path(
          "ingredients/",
          views.get_ingredients,
          name="get_ingredients"
     ),
     path(
          "subscriptions",
          views.follow,
          name="follow"
     ),
     path(
          "subscriptions/<int:follow_pk>",
          views.unfollow,
          name="unfollow"
     ),
     path(
          "favorites",
          views.in_favor,
          name="in_favor"
     ),
     path(
          "favorites/<int:favor_pk>",
          views.out_favor,
          name="out_favor"
     ),
     path(
          "purchases",
          views.in_list,
          name="in_list"
     ),
     path(
          "purchases/<int:purch_pk>",
          views.out_list,
          name="out_list"
     ),
     path(
          "download",
          views.download,
          name="download"
     ),
]
