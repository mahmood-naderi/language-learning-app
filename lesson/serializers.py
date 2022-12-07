# directiories
from knowledge_graph.models import Context, Lexical
from .models import Exercise_Model, Mistake
from knowledge_graph.serializers import Lexical_Serializer
from user.serializers import User_Serializer

# rest framework
from rest_framework import serializers


class Context_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = "__all__"

class Exercise_Serializer(serializers.ModelSerializer):
    option1 = Lexical_Serializer()
    option2 = Lexical_Serializer()
    option3 = Lexical_Serializer()
    option4 = Lexical_Serializer()
    answer = Lexical_Serializer()
    context = Context_Serializer()
    # image = serializers.SerializerMethodField()
        

    class Meta:
        model = Exercise_Model
        fields = "__all__"

    # def get_image(self, obj):
    #     return self.context['request'].build_absolute_uri(obj.image.url)
class Mistake_Serializer(serializers.ModelSerializer):
    user = User_Serializer()
    word = Lexical_Serializer()
    context = Context_Serializer()
    class Meta:
        model = Mistake
        fields = "__all__"


class Mistake_Add_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mistake
        fields = "__all__"

