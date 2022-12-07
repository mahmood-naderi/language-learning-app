from django.db import models

class Context(models.Model):
    context = models.CharField(max_length = 25, null=True)
    meaning = models.CharField(max_length = 25)
    weight = models.FloatField(null=True)

    def __str__(self):
        return self.meaning

class Lexical(models.Model):
    context = models.ForeignKey(Context, null = True, on_delete = models.SET_NULL)
    word = models.CharField(max_length = 25)
    meaning = models.CharField(max_length = 25)
    weight = models.FloatField(null = True)

    def __str__(self):
        return self.word


class Skill(models.Model):
    word = models.ForeignKey(Lexical, on_delete = models.CASCADE)
    listening_weight = models.IntegerField()
    reading_weight = models.IntegerField()
    writing_weight = models.IntegerField()




