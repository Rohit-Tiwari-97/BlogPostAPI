from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogapi import views

# Creating a router and registering our viewsets with it.
router = DefaultRouter()
router.register(r'create', views.BlogCreateViewSet,basename="create")
router.register(r'blogs', views.BlogPostsViewSet,basename="blogs")
router.register(r'users', views.UserViewSet,basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]