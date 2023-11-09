from django.urls import path
from . import views


urlpatterns = [
  path('', views.fetch_all_videos),
  path('post', views.post_video),
  path('<int:id>', views.view_edit_video)
]