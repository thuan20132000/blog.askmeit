
from reading.models import ReadingTopic, ReadingPost, ReadingPostVocabulary

from rest_framework.decorators import api_view
from rest_framework.response import Response
from reading.serializers import ReadingTopicSerializer, ReadingPostSerializer, PaginationBaseCustom, ReadingPostDetailSerializer,ReadingPostVocabularySerializer


from reading.helper import log_message


@api_view(['GET'])
def get_reading_topic_list(request):
    try:

        topic_list = ReadingTopic.objects.filter(
            status='published').all()
        serializer = ReadingTopicSerializer(topic_list, many=True).data
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
def get_reading_post_list(request,):
    try:

        topic_id = request.query_params.get('topic')
        if topic_id:
            post_list = ReadingPost.objects.filter(
                status='published', reading_topic_id=topic_id).order_by('-updated_at').all()
        else:
            post_list = ReadingPost.objects.filter(
                status='published').order_by('-updated_at').all()

        paginator = PaginationBaseCustom()
        paginator.page_size = 10
        context = paginator.paginate_queryset(post_list, request)
        serializer = ReadingPostSerializer(context, many=True).data

        return Response(paginator.get_paginated_response(serializer))


    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })


@api_view(['GET'])
def get_reading_post_detail(request, readingpost_id):
    try:

        reading_post = ReadingPost.objects.get(pk=readingpost_id)
        serializer = ReadingPostDetailSerializer(reading_post).data
        return Response({
            "status": True,
            "message": f"Get post detail successfully",
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
def get_reading_post_vocabulary(request, readingpost_id):
    try:

        reading_post = ReadingPostVocabulary.objects.filter(
            reading_post_id=readingpost_id, status='published').all()

        serializer = ReadingPostVocabularySerializer(reading_post,many=True).data

        return Response({
            "status": True,
            "message": f"Get readingpost vocabulary successfully",
            "data": serializer
        })

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })
