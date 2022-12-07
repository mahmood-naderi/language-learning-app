# django

# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# directories
from .models import Lexical
from .serializers import Lexical_Serializer

class Lexical_Knowledge_Graph(APIView):
    serializer_class = Lexical_Serializer

    # add words to the knowledge gragh
    def post(self, request, *args, **kwargs):
        serialized_word = self.serializer_class(data = request.data)
        serialized_word.is_valid()

        serialized_word.save()

        return Response(serialized_word.data, status = status.HTTP_200_OK)

    # retrieve words from the knowledge graph
    def get(self, request, *args, **kwargs):
        try:
            words_query = Lexical.objects.all()
            serialized_words = self.serializer_class(words_query, many = True)

            return Response(serialized_words.data, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)