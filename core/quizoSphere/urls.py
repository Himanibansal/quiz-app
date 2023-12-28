from django.contrib import admin
from django.urls import path
from quizoSphere.views import *
urlpatterns = [
   path('get_quiz',get_quiz,name="get_quiz"),
   # path('question',question,name="question"),
   path('question/<int:quiz_id>/', question, name='question'),  # Use the same name as in the template

   
]
