
from reading.models import ReadingTopic,ReadingPost

from rest_framework.decorators import api_view
from rest_framework.response import Response
from reading.serializers import ReadingTopicSerializer,ReadingPostSerializer,PaginationBaseCustom



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
def get_reading_post_list(request):
    try:

        post_list = ReadingPost.objects.filter(
            status='published').order_by('-updated_at').all()

        paginator = PaginationBaseCustom()
        paginator.page_size = 10
        context = paginator.paginate_queryset(post_list,request)
        serializer = ReadingPostSerializer(context, many=True).data

        return Response(paginator.get_paginated_response(serializer))


        # return Response({
        #     "status": True,
        #     "message": f"Get post list successfully",
        #     "data": serializer
        # })

    except Exception as e:
        message = f"error: {e}"
        log_message(message)
        return Response({
            "status": False,
            "message": f"error : {e}"
        })


@api_view(['GET'])
def get_reading_post_detail(request,readingpost_id):
    try:

        reading_post = ReadingPost.objects.get(pk=readingpost_id)
        serializer = ReadingPostSerializer(reading_post).data
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