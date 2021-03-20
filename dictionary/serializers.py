
from rest_framework import serializers
from dictionary.models import Vocabulary





class VocabularyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields  = ['id','name','phon_us','phon_uk','sound_us','sound_uk']



class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'
        # exclude = ['updated_at','created_at','status','topic','certification_field']

