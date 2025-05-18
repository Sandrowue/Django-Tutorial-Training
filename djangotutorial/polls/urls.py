from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    # example without generic views:
    """ path("", views.index, name="index"), """
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    # example without generic views:
    """ path("<int:question_id>/", views.detail, name="detail"), """
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    # example without generic views:
    """ path("<int:question_id>/results/", views.results, name="results"), """
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]