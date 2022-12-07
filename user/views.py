# django
# rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# directories
from .models import User
from .serializers import User_Serializer

class User_Manager(APIView):
    serializer_class = User_Serializer

    # retrieve list of all users
    def get(self, request, *args, **kwargs):
        user_query = User.objects.all()
        serialized_users = self.serializer_class(user_query, many = True)

        return Response(serialized_users.data, status = status.HTTP_200_OK)

    # create a user
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid()

        serializer.save()

        return Response(serializer.data ,status = status.HTTP_200_OK)

