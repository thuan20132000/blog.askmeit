from rest_framework import serializers
from flashcard.models import VocabularyCard, Topic,Field


class TopicSerializer(serializers.ModelSerializer):


    vocabulary_total = serializers.SerializerMethodField('get_topic_vocabulary_number')
    
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 2

    def get_topic_vocabulary_number(self,obj):
        total = VocabularyCard.objects.filter(topics=obj).count()
        # return VocabularyCardSerializer(vocabulary_list,many=True).data
        return total
class VocabularyCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = VocabularyCard
        depth = 2
        fields = '__all__'


    
class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        depth = 1
        fields = '__all__'