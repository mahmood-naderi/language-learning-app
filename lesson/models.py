from django.db import models

# directories
from knowledge_graph.models import Context, Lexical
from user.models import User

class Exercise_Model(models.Model):
    image = models.ImageField()
    context = models.ForeignKey(Context, on_delete = models.CASCADE)
    exercise_type = models.IntegerField()
    option1 = models.ForeignKey(Lexical, on_delete = models.CASCADE, related_name = "option1")
    option2 = models.ForeignKey(Lexical, on_delete = models.CASCADE, related_name = "option2")
    option3 = models.ForeignKey(Lexical, on_delete = models.CASCADE, related_name = "option3")
    option4 = models.ForeignKey(Lexical, on_delete = models.CASCADE, related_name = "option4")
    answer = models.ForeignKey(Lexical, on_delete = models.CASCADE)

class Mistake(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    word = models.ForeignKey(Lexical, on_delete = models.CASCADE)
    context = models.ForeignKey(Context, on_delete = models.CASCADE, default = 1)

class Learned_Context(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    context = models.ForeignKey(Context, on_delete = models.CASCADE)
    score = models.IntegerField(null = True)

class Learned_Word(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    word = models.ForeignKey(Lexical, on_delete = models.CASCADE)
    score = models.IntegerField(null = True)
    times = models.IntegerField(default=1)
