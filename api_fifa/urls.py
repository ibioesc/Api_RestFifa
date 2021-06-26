from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from team_players.views import PlayersRequestViewSet,TeamRequestViewSet
router = DefaultRouter()

# router.register(r'teams',TeamsRequestViewSet)
router.register(r'team/',TeamRequestViewSet)
router.register(r'players/',PlayersRequestViewSet)
urlpatterns= router.urls
urlpatterns += [
    path('admin/', admin.site.urls)
]
