from django.shortcuts import render
from itertools import chain
from django.db.models import Q


# directoris
from knowledge_graph.models import Context
from .serializers import Context_Serializer, Exercise_Serializer, Mistake_Serializer, Mistake_Add_Serializer
from .models import Exercise_Model, Mistake, Learned_Word, Learned_Context
from user.models import User
from dictionary.models import Dictionary
from knowledge_graph.models import Lexical, Context

# restframework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class Context_Manager(APIView):
    serializer_class = Context_Serializer

    def get(self, request, *args, **kwargs):
        query = Context.objects.all()
        serializer = self.serializer_class(query, many = True)
        return Response(serializer.data ,status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status = status.HTTP_201_CREATED)

class Exercise_Manager(APIView):
    serializer_class = Exercise_Serializer

    def get(self, request, *args, **kwargs):
        exercise_query = Exercise_Model.objects.all()
        serialized_exercise = self.serializer_class(exercise_query, many = True, context={'request': request})
        # serialized_exercise.is_valid()

        return Response(serialized_exercise.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            serialized_exercise = self.serializer_class(data = request.data)
            serialized_exercise.is_valid()

            serialized_exercise.save()
            return Response(status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class Report_Answer(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data["type"])
        if request.data["type"] == '1':
            user = User.objects.get(email = request.data["email"])
            lexical = Lexical.objects.get(word = request.data["word"])
            context_word = lexical.context
            
            words_of_context = Lexical.objects.filter(context = context_word)

            # print(Learned_Word.objects.get(user = user, word = lexical).exists())
            if Learned_Word.objects.filter(user = user, word = lexical).exists():
                word_obj = Learned_Word.objects.get(user = user, word = lexical)
                word_obj.score = ((word_obj.score * word_obj.times) + 100) / (word_obj.times + 1)
                word_obj.times = word_obj.times + 1
                word_obj.save(update_fields=["score", "times"])

            else:
                learned_word = Learned_Word(user = user, word = lexical, score = 100, times = 1)
                learned_word.save()
            
            new_score = 0
            for item in words_of_context:
                if Learned_Word.objects.filter(user = user, word = item).exists():
                    learned_word_exists = Learned_Word.objects.filter(user = user, word = item)
                    if item.weight == None:
                        new_score += learned_word_exists[0].score * 0
                        print(new_score)
                    else:
                        new_score += learned_word_exists[0].score * item.weight
                        print(new_score)
            
            user_context = Learned_Context.objects.get(user = user, context = context_word)
            user_context.score = new_score
            user_context.save(update_fields=["score"])


        elif request.data["type"] == '0':
            user = User.objects.get(email = request.data["email"])
            lexical = Lexical.objects.get(word = request.data["word"])
            # print(Learned_Word.objects.get(user = user, word = lexical).exists())
            if Learned_Word.objects.filter(user = user, word = lexical).exists():
                word_obj = Learned_Word.objects.get(user = user, word = lexical)
                word_obj.score = ((word_obj.score * word_obj.times) + 0) / (word_obj.times + 1)
                word_obj.times = word_obj.times + 1
                word_obj.save(update_fields=["score", "times"])
            else:
                
                learned_word = Learned_Word(user = user, word = lexical, score = 0, times = 1)
                learned_word.save()

        return Response(status = status.HTTP_200_OK)

class Add_Mistake(APIView):
    serializer_class = Mistake_Add_Serializer
    def post(self, request, *args, **kwargs):
        serialized_mistake = self.serializer_class(data = request.data)
        serialized_mistake.is_valid()
        serialized_mistake.save()

        return Response(serialized_mistake.data, status = status.HTTP_200_OK)

class Random_exersice(APIView):
    serializer_class = Exercise_Serializer

    def get(self, request, email, context, *args, **kwargs):
        user = User.objects.get(email = email)
        print(user.id)
        mistakes = Mistake.objects.filter(user = user)
        dict_words = Dictionary.objects.filter(user = user)
        mistakes_list = []
        for item in mistakes:
            # print(item.word)
            mistakes_list.append(item.word)
            # print("----------------------------")

        for item in dict_words:
            if item.word not in mistakes_list:
                mistakes_list.append(item.word)

        # for item in mistakes_list:
        #     print(item)
        #     # mistakes_list.append(item.word)
        #     print("----------------------------")
        
        exercise_queryset = Exercise_Model.objects.none()
        for word in mistakes_list:
            exercise_query = Exercise_Model.objects.filter(Q(option1 = word) | Q(option2 = word) | Q(option3 = word) | Q(option4 = word))
            print(word)
            exercise_queryset = list(chain(exercise_queryset, exercise_query))

        serialized_query = self.serializer_class(exercise_queryset, many = True)
        # for item in serialized_mistakes.data:
        #     print(item.items())
        #     print("----------------------------")
        return Response(serialized_query.data)
        # return Response(status = status.HTTP_200_OK)
