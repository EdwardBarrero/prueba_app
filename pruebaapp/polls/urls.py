from django.urls import path

from . import views

app_name = "polls"
urlpatterns=[
  path("", views.IndexView.as_view(), name="index"),
  path("detail/<int:pk>", views.DetailView.as_view(), name="detail"),
  path("result/<int:pk>", views.ResultsView.as_view(), name="results"),
  path("votes/<int:question_id>", views.votes, name="votes")
]