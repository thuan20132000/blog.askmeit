
from rest_framework import serializers
from reading.models import ReadingTopic,ReadingPost,ReadingPostVocabulary

from rest_framework.pagination import PageNumberPagination, BasePagination



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

class ReadingTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingTopic
        fields = '__all__'
        depth = 1

    

class ReadingPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingPost
        depth = 1
        exclude = ['content']




class ReadingPostVocabularySerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingPostVocabulary
        fields = '__all__'




class ReadingPostVocabularyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingPostVocabulary
        fields = ['name']

class ReadingPostDetailSerializer(serializers.ModelSerializer):


    reading_post_vocabulary = serializers.SerializerMethodField('get_reading_post_vocabulary')

    class Meta:
        model = ReadingPost
        depth = 1
        fields = ['title','slug','content','reading_topic','created_at','reading_post_vocabulary']

    
    def get_reading_post_vocabulary(self,obj):
        post_vocabulary_list = obj.reading_post.values('name','pk').all()

        return post_vocabulary_list

        # return ReadingPostVocabularyNameSerializer(post_vocabulary_list,many=True).data 