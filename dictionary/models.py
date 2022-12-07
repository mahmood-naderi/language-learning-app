# django
from django.db import models

# directories
from knowledge_graph.models import Lexical
from user.models import User

class Dictionary(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    word = models.ForeignKey(Lexical, on_delete = models.CASCADE)
    time_added = models.DateField(auto_now_add = True)