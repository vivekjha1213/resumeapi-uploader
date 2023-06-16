import statistics
from fastapi import Response
from rest_framework import serializers

from api.views import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ['id', 'name', 'email', 'dob',
                  'state', 'gender', 'location', 'pimage', 'rdoc']

    def save_profile(request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile saved successfully'}, status=statistics.HTTP_201_CREATED)
        return Response(serializer.errors)
