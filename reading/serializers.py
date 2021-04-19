
from rest_framework import serializers
from reading.models import ReadingTopic,ReadingPost

from rest_framework.pagination import PageNumberPagination, BasePagination


class ReadingTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingTopic
        fields = '__all__'
        depth = 1

    

class ReadingPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingPost
        depth = 1
        fields = '__all__'


    
class PaginationBaseCustom(PageNumberPagination):

    def get_paginated_response(self, data, **kwargs):
        response_dict = dict()
        for key, value in kwargs.items():
            response_dict[key] = value

        response_dict["status"] = True
        response_dict["count"] = self.page.paginator.count
        response_dict["next"] = self.get_next_link()
        response_dict["previous"] = self.get_previous_link()
        response_dict["limit"] = self.page_size
        response_dict["data"] = data

        return response_dict