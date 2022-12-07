# django
from django.shortcuts import render

# rest framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# directories
from user.models import User
from user.serializers import User_Serializer
from dictionary.models import Dictionary
from knowledge_graph.models import Lexical
from .serializers import Dictionary_Retrieve_Serializer, Dictionary_Add_Serializer

class Add_Word_To_Dictionary(APIView):
    serializer_class = Dictionary_Add_Serializer

    def post(self, request, *args, **kwargs):
        try:
            # user = User.objects.get(email = request.data['email'])
            # word = Lexical.objects.get(word = request.data['word'])
            # new_word = Dictionary(word = word, user = user)
            # new_word.save()

            serialized_word = self.serializer_class(data = request.data)
            user = User.objects.get(email = request.data["user"])
            serialized_word.is_valid()
            word = Lexical.objects.get(word = request.data["word"])
            dict_obj = Dictionary(user = user, word = word)
            dict_obj.save()
            # serialized_word.save()
            return Response(serialized_word.data, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class Get_User_Dictionary(APIView):
    serializer_class = Dictionary_Retrieve_Serializer
    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        user = User.objects.get(email = email)
        dictionary_words = Dictionary.objects.filter(user = user.id).order_by("time_added")
        serialized_words = self.serializer_class(dictionary_words, many = True)
        print(user)

        return Response(serialized_words.data)