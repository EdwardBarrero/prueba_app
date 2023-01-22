from django.urls import path

from . import views

urlpatterns=[
  path("", views.index, name="index"),
  path("<int:question_id>", views.detail, name="detail"),
  path("result/<int:question_id>", views.results, name="results"),
  path("votes/<int:question_id>", views.votes, name="votes")
]