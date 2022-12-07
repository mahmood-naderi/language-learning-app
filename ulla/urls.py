"""ulla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lesson.views import Context_Manager, Exercise_Manager, Random_exersice, Add_Mistake, Report_Answer
from dictionary.views import Add_Word_To_Dictionary, Get_User_Dictionary
from knowledge_graph.views import Lexical_Knowledge_Graph
from user.views import User_Manager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson/context/', Context_Manager.as_view(), name = "context"),
    path('dictionary/save/', Add_Word_To_Dictionary.as_view(), name = "save-dictionary"),
    path('dictionary/get/', Get_User_Dictionary.as_view(), name = "get-dictionary"),
    path('lesson/exercise/<int:id>', Exercise_Manager.as_view(), name = "exercises"),
    path('lesson/exercise/random/<int:context>/<str:email>/', Random_exersice.as_view(), name = "random-exercise"),
    path('lesson/mistake/', Add_Mistake.as_view(), name = 'mistake'),
    path('lesson/report/', Report_Answer.as_view(), name = 'report'),
    path('kgraph/lexical/', Lexical_Knowledge_Graph.as_view(), name = "lexical"),
    path('users/', User_Manager.as_view(), name = "users"),
]