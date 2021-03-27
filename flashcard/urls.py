
from django.urls import path,include


from flashcard import api



urlpatterns = [
    path('topic/',api.get_topic_list,name="get_topic_list"),
    path('topic/<int:topic_id>/vocabulary',api.get_topic_vocabulary,name="get_topic_vocabulary"),
    
]