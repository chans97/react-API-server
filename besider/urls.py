from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from game.views import UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('game.urls')),
]
