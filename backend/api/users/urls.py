from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_user, name="login"),
    path("register", views.register_user, name="register"),
    path("user_data", views.get_user_data, name="user_data"),
    path(
        "fetch/<int:id>",
        views.fetch_specific_user_by_id,
        name="fetch_specific_user_by_id",
    ),
    path("update/<int:id>", views.update_user_by_id, name="update_user_by_id"),
    path("delete/<int:id>", views.delete_user_by_id, name="delete_user_by_id"),
]
