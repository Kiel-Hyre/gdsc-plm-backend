from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response # NOTE THIS INSTEAD OF HTTPRESPONSE OR RENDER we use this
from django.views.decorators.csrf import csrf_exempt
# https://www.django-rest-framework.org/api-guide/views/

from rest_framework.parsers import JSONParser

from . import models
from . import serializers # note were not using forms

@api_view() # GET by default  @api_view(['GET'])
def api(request):
    context = {
        'name': 'Miguel',
        #'to_do': models.Action.objects.all(), # this will cause an error, all data should be serialize or non-object
        'to_do': models.Action.objects.all().values('id', 'text', 'description')

        # another approach was to use serialize as outside response
        # 'to_do': serializers.ActionSerializer(models.Action.objects.all(), many=True).data
        # https://www.django-rest-framework.org/api-guide/serializers/
        # this approach is much better
    }
    return Response(context) # status by default is 200

@api_view()
def api_view(request, pk):
    obj = get_object_or_404(models.Action, pk=pk)
    # NOTE IN THIS FUNCTION WERE ONLY FOCUSING ON TRANSFERRING BACK A SERIALIZED OBJECT
    # AND NOT WORRYING ABOUT TEMPLATES OR REDIRECTS
    return Response({'data':serializers.ActionSerializer(obj).data})


# FOR SOME REASON api_view decorator is bugging therefore use this
from rest_framework.views import APIView

class APIDeleteView(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(models.Action, pk=pk)
        obj.delete()
        return Response({'data': True})


class APICreateView(APIView):
    def post(self, request):
        serializer = serializers.ActionAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = models.Action.objects.create(**serializer.validated_data)
        return Response(serializers.ActionSerializer(obj).data)


class APIUpdateView(APIView):
    def post(self, request, pk):
        obj = get_object_or_404(models.Action, pk=pk)
        serializer = serializers.ActionUpdateSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)

        # normal
        for k, v in serializer.validated_data.items():
            setattr(obj, k, v)
        obj.save()

        return Response(serializers.ActionSerializer(obj).data)


# DIY, make a model serializer counterpart of those serializer :)
# Another there was a create and update method in the serializer itself