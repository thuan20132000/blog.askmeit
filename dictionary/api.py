from dictionary.models import Vocabulary
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dictionary.serializers import VocabularySerializer, VocabularyBaseSerializer

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from dictionary.helper import log_message


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

        vocabulary_list = Vocabulary.objects.filter(name__startswith=query).all()[:10]
        vocabulary_list_serializers = VocabularyBaseSerializer(
            vocabulary_list, many=True).data
        return Response({
            "status": True,
            "message": "Success",
            "data": vocabulary_list_serializers
        })

    except Exception as e:
        log_message(f"error: {e}")
        return Response({
            "status": False,
            "message": f"error: {e}"
        })


@api_view(['GET'])
def get_detail_vocabulary(request, vocabulary_id):
    try:
        vocabulary = Vocabulary.objects.get(ID=vocabulary_id)
        vocabulary_serializer = VocabularySerializer(vocabulary).data

        return Response({
            "status": True,
            "message": "Success",
            "data": vocabulary_serializer
        })

    except Exception as e:
        log_message(f"error: {e}")

        return Response({
            "status": False,
            "message": f"error: {e}"
        })
