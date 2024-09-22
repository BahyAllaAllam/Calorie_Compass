from rest_framework import serializers
from .models import Meals


class MealSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Meals
        fields = ['id', 'user', 'name', 'food_items', 'calories', 'created_at', 'date']
        read_only_fields = ['date']