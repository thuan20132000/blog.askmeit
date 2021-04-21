from django.urls import path,include

from reading import api


urlpatterns = [
    path('api/v1/readingtopics/',api.get_reading_topic_list,name='get_reading_topic_list'),
    path('api/v1/readingposts/',api.get_reading_post_list,name='get_reading_post_list'),
    path('api/v1/readingpost/<int:readingpost_id>',api.get_reading_post_detail,name="get_reading_post_detail"),
    path('api/v1/readingpost/<int:readingpost_id>/vocabulary/',api.get_reading_post_vocabulary,name="get_reading_post_vocabulary"),
]