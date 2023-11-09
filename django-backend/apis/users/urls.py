from django.urls import path
from . import views


urlpatterns = [
  path('', views.get_all_users),
  path('user_data', views.get_user_data),
  path('register', views.register_user),
  path('login', views.login_user),
  path('<int:id>', views.view_edit_user)
]