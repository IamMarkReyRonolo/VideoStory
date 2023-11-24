from django.urls import path
from . import views


urlpatterns = [
    path("", views.fetch_all_videos, name="fetch_all_videos"),
    path("post", views.post_video, name="post_video"),
    path(
        "fetch/<int:id>",
        views.fetch_specific_video_by_id,
        name="fetch_specific_video_by_id",
    ),
    path("update/<int:id>", views.update_video_by_id, name="update_video_by_id"),
    path("delete/<int:id>", views.delete_video_by_id, name="delete_video_by_id"),
]
