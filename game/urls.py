from django.urls import path

from .views import UserByLevelView

urlpatterns = [
    path('level/<int:level>/', UserByLevelView.as_view()),
]