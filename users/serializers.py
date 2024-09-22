from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'image', 'age', 'height', 'weight']


    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.age = validated_data.get('age', instance.age)
        instance.hight = validated_data.get('height', instance.hight)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance
