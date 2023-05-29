from rest_framework import serializers
from .models import User

class FollowSerializer(serializers.ModelSerializer):
    followers = serializers.IntegerField(source='user.followers.count()', read_only=True)
    followings = serializers.IntegerField(source='user.followings.count()', read_only=True)

    class Meta:
        model = User
        fields = ('followers', 'followings')

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class YourpageSerializer(serializers.ModelSerializer):
    followers = FollowerSerializer(many=True, read_only=True)
    # followers = serializers.CharField(source='user.followers', read_only=True)
    followings = FollowerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'followers', 'followings', 'point')
        