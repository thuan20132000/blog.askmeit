from django.urls import path,include

from dictionary.api import (
    get_search_vocabulary
)

urlpatterns = [
    path('api/v1/search',get_search_vocabulary,name="search_vocabulary"),

]