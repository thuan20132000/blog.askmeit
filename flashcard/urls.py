
from django.urls import path,include


from flashcard import api



urlpatterns = [
    path('api/v1/topic/',api.get_topic_list,name="get_topic_list"),
    path('api/v1/topic/<int:topic_id>/vocabulary',api.get_topic_vocabulary,name="get_topic_vocabulary"),
    
]