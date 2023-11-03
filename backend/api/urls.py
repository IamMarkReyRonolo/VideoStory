from django.urls import path
from . import views


urlpatterns = [
  path('', views.fetch_all_videos),
  path('upload', views.post_video),
  path('<int:id>', views.video_detail)
]