from django.shortcuts import render
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from .models import Favourite, Law
from .Serializer import FavouriteSerializer, WictFavouriteSerializer
#from Project.models import Law
# Create your views here.
from rest_framework.decorators import permission_classes


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def lawfavourites(request):
    if request.method == "GET":
        favoultes_list = Favourite.objects.filter(user=request.user)
        data = FavouriteSerializer(favoultes_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        izb_id = request.data["izb_id"]
        Favourite.objects.create(izb_id=izb_id,
                                      user=request.user)
        return Response(data={"message": "Favourite created"})
    elif request.method == "DELETE":
        izb_id = request.data["izb_id"]
        Favourite.objects.filter(izb_id=izb_id,
                                      user=request.user).delete()

        return Response(data={"message": "Favourite deleted!"})


@api_view(["GET"])
def law_wits_favourite(request):
    izb = Law.objects.all()
    data = WictFavouriteSerializer(izb, many=True, context={"request": request}).data

    return Response(data=data)