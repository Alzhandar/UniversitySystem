from django.urls import path, include
from .views import TestUserView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('test/', TestUserView.as_view(), name='test-user'),
]