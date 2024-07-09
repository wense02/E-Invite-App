from rest_framework import generics, permissions, status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from .models import Invite
from .serializers import InviteSerializer, UserSerializer
from .utils import send_invite_email
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError

@api_view(['POST'])
def register(request):
    data = request.data
    print(f"Received data: {data}")
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username:
        print("Username is missing")
        return Response({'error': 'Username is required.'}, status=status.HTTP_400_BAD_REQUEST)
    if not email:
        print("Email is missing")
        return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
    if not password:
        print("Password is missing")
        return Response({'error': 'Password is required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(password)
    except ValidationError as e:
        print(f"Password validation failed: {e.messages}")
        return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        print("Username already taken")
        return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        print("Email already registered")
        return Response({'error': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    print("User created successfully")
    return Response({'success': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


def test_email(request):
    try:
        send_mail(
            'Test Email',
            'This is a test email sent from Django.',
            settings.EMAIL_HOST_USER,
            ['recipient@example.com'],
            fail_silently=False,
        )
        return HttpResponse('Email sent successfully')
    except SMTPException as e:
        return HttpResponse(f'Failed to send email: {e}', status=500)

class InviteListCreate(generics.ListCreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer


class InviteListCreate(generics.ListCreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        invite = serializer.save()
        invite_link = f"https://osheaobajoseph3.wixsite.com/potterslounge/event-details/qavah/"  # Adjust to your invite acceptance URL
        send_invite_email(invite.name, invite.email, invite_link)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  
