from django.urls import path
from .views import InviteListCreate, UserCreate, test_email, RegisterView

urlpatterns = [
    path('invites/', InviteListCreate.as_view(), name='invite-list-create'),
    path('register/', UserCreate.as_view(), name='user-create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('test-email/', test_email, name='test-email'),
]