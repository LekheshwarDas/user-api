from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # This view handles GET and POST requests for the User model.
    # It lists all users and creates a new user.

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # This view handles GET, PUT, PATCH, and DELETE requests for a specific user.
    # It retrieves, updates, or deletes a user based on the provided ID.