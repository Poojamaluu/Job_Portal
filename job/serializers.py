from django.contrib.auth.models import User

from rest_framework import serializers

from job.models import Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        u= User.objects.create_user(**validated_data)
        u.save()
        return u

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('posted_by',)