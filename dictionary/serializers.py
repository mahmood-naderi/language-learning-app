from rest_framework import serializers
from user.serializers import User_Serializer
from knowledge_graph.serializers import Lexical_Serializer
from .models import Dictionary

class Dictionary_Add_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = "__all__"

class Dictionary_Retrieve_Serializer(serializers.ModelSerializer):
    user = User_Serializer()
    word = Lexical_Serializer()
    class Meta:
        model = Dictionary
        fields = "__all__"