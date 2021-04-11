
from django.urls import path,include


from flashcard import api



urlpatterns = [
    path('api/v1/topic/',api.get_topic_list,name="get_topic_list"),
    path('api/v1/topic/<int:topic_id>/vocabulary',api.get_topic_vocabulary,name="get_topic_vocabulary"),
    path('api/v1/fields/',api.get_fields,name="get_fields_list"),
    path('api/v1/field/<int:field_id>',api.get_field_topic,name="get_field_topic"),
]