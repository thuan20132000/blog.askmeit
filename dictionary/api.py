from dictionary.models import Vocabulary
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dictionary.serializers import VocabularySerializer, VocabularyBaseSerializer

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank


@api_view(['GET'])
def get_search_vocabulary(request):

    try:

        query = request.query_params.get('qquery')

        search_vector = SearchVector("name")
        search_query = SearchQuery(query)

        # vocabulary = Vocabulary.objects.annotate(
        #     search=search_vector
        # ).filter(search=search_query)
        # print('data: ',vocabulary)

        vocabulary_list = Vocabulary.objects.filter(name__startswith=query).values(
            'name', 'id', 'phon_us', 'phon_uk', 'sound_us', 'sound_uk').all()
        vocabulary_list_serializers = VocabularyBaseSerializer(
            vocabulary_list, many=True).data
        return Response({
            "status": True,
            "message": "Success",
            "data": vocabulary_list_serializers
        })

    except Exception as e:

        return Response({
            "status": False,
            "message": f"error: {e}"
        })


@api_view(['GET'])
def get_detail_vocabulary(request,vocabulary_id):
    try:
        vocabulary = Vocabulary
    except Exception as e:
        return Response({
            "status": False,
            "message": f"error: {e}"
        })
