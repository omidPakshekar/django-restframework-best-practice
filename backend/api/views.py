import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
         django rest_framework view
    """
    serializer_ = ProductSerializer(data= request.data)
    if serializer_.is_valid(raise_exception=True):
        #%%%%%%%%%%%%
        # serializer_.save()
        data = serializer_.data
        return Response(data)

    return Response({"invalid" : "not good data"}, status=400)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#          django rest_framework view
#     """
#     instamce = Product.objects.all().order_by('?').first()
#     data = {}
#     if instamce:
#         data = ProductSerializer(instamce).data
#     return Response(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#
#     return JsonResponse(data)



# def api_home(request, *args, **kwargs):
#     # request -> httpRequset --> Django
#
#     body = request.body #
#     data = {}
#     try:
#         data = json.loads(body)
#     except Exception as e:
#         pass
#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#
#     return JsonResponse(data)
