from django.urls import path

from .views import UserByLevelView, PostListView,ReplViewSet

urlpatterns = [
    path('<int:id>/', UserByLevelView.as_view()),
    path('list/', PostListView.as_view()),
    path('repl/', ReplViewSet.as_view()),
]