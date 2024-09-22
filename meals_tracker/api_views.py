from rest_framework import viewsets
from .models import Meals
from .serializers import MealSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all().order_by('-created_at')
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Check if this is a Swagger schema generation request
        if getattr(self, 'swagger_fake_view', False):
            return Meals.objects.none()  # Return an empty queryset for schema generation


        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Meals.objects.all().order_by('-created_at')
        elif isinstance(user, AnonymousUser):
            return Meals.objects.none()  # Prevent anonymous users from accessing meals
        return Meals.objects.filter(user=user).order_by('-created_at')
