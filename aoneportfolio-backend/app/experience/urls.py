"""
URL mappings for the experience API.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from experience import views


router = DefaultRouter()
router.register('experiences', views.ExperienceViewSet)

app_name = 'experiences'

urlpatterns = [
    path('', include(router.urls)),
]
