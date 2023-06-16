from rest_framework.response import Response
# from traitlets import Type
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework import status
from rest_framework.views import APIView


class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Profile.objects.filter(email=email).exists():
                # Return a response with a 400 status code if the email already exists
                return Response({'message': 'Email already exists', 'status': 'failed', 'candidate': serializer.data}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            # Return a response with a 201 status code indicating success
            return Response({'message': 'Profile created', 'status': 'success', 'candidate': serializer.data}, status=status.HTTP_201_CREATED)
        
        # Return a response with serializer errors if it is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def get(self, request, format=None):
    #     candiates = Profile.objects.all()
    #     serializer = ProfileSerializer(candiates, many=True)
    #     return Response({'status': 'Success', 'candiate': serializer.data},
    #                     status=status.HTTP_200_OK)

    def get(self, request, format=None):
        try:
            candiates = Profile.objects.all()
            serializer = ProfileSerializer(candiates, many=True)
            return Response({'status': 'Success', 'candiate': serializer.data},
                        status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
          return Response({'message': 'No credentials for the user'}, status=status.HTTP_404_NOT_FOUND)
