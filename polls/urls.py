from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # /polls
    path("polls/", views.IndexView.as_view(), name="index"),

    # /polls/1
    path("polls/<int:pk>/", views.DetailView.as_view(), name="detail"),

    # /polls/1/vote
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),

    # /polls/1/results
    path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results"),


    path("", views.index, name="index"),

    path("purchase/", views.purchase, name="purchase"),

    path("confirmation/", views.order_confirmation, name="order_confirmation"),
]
