from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("quiz/<int:quiz_id>", views.quiz_detail, name="quiz_detail"),
               path("quiz/<int:quiz_id>/submit", views.quiz_submit, name="quiz_submit")]