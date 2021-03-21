from django.urls import path,include

from dictionary.api import (
    get_search_vocabulary,
    get_detail_vocabulary
)

urlpatterns = [
    path('api/v1/search',get_search_vocabulary,name="search_vocabulary"),
    path('api/v1/vocabulary/<int:vocabulary_id>',get_detail_vocabulary,name="detail_vocabulary"),

]