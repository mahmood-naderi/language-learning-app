# rest framework
from rest_framework import serializers

# directories
from .models import Lexical

class Lexical_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lexical
        fields = "__all__"