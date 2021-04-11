

from flashcard.models import VocabularyCard, Topic, Field
from rest_framework.decorators import api_view
from rest_framework.response import Response
from flashcard.serializers import TopicSerializer, VocabularyCardSerializer, FieldSerializer


from flashcard.helper import log_message


@api_view(['GET'])
def sample(request):
    try:

        pass

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })


@api_view(['GET'])
def get_topic_list(request):
    try:

        topic_list = Topic.objects.filter(
            status='published').all()
        serializer = TopicSerializer(topic_list, many=True).data
        return Response({
            "status": True,
            "message": f"Get topic list successfully",
            "data": serializer
        })

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })


@api_view(['GET'])
def get_topic_vocabulary(request, topic_id):
    try:

        topic_vocabulary = VocabularyCard.objects.filter(
            topics__id=topic_id).all()

        serializer = VocabularyCardSerializer(topic_vocabulary, many=True).data

        return Response({
            "status": True,
            "message": f"Get vocabulary successfully with topic_id {topic_id}",
            "data": serializer
        })

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })


@api_view(['GET'])
def get_field_topic(request, field_id):
    try:
        topic_list = Topic.objects.filter(
            field_id=field_id, status='published').all()
        serializer = TopicSerializer(topic_list, many=True).data
        return Response({
            "status": True,
            "message": f"Get field topic list successfully",
            "data": serializer
        })

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })


@api_view(['GET'])
def get_fields(request,):
    try:
        fields_list = Field.objects.filter(status='published').all()
        serializer = FieldSerializer(fields_list, many=True).data
        return Response({
            "status": True,
            "message": f"Get field  successfully",
            "data": serializer
        })

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })
