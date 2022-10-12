"""
ptwt URL Configuration
"""
from django.urls import path, include
from rest_framework import routers
from ptwt.views import TweetViewSet, index

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet, basename='tweet')

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('tweets/tweet/<int:pk>', TweetViewSet.as_view({'delete': 'destroy'}), name='delete-tweet'),
]
