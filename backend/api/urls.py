from django.urls import path
from . import views
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("notes/update/<int:pk>/", views.NoteUpdate.as_view(), name="update-note"),  
    path("register/", CreateUserView.as_view(), name="register"),  # Перенесено из backend/urls.py
    path("token/", TokenObtainPairView.as_view(), name="get_token"),  # Перенесено из backend/urls.py
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),  # Перенесено из backend/urls.py
]

