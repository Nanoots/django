from django.urls import include, path
from rest_framework import routers

from . import views
from .api import PostViewSet

app_name = "blog"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("api/", include(router.urls)),
]
