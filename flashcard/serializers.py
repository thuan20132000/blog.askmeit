from rest_framework import serializers
from flashcard.models import VocabularyCard, Topic


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class VocabularyCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = VocabularyCard
        depth = 1
        fields = '__all__'
