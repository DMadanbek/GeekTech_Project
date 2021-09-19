from django.shortcuts import render
from .models import News, ImageNews, Law
from .Serializer import NewsListSerializer, NewsItemSerializer, LawItemSerializer, LawListSerializer, LawFilter
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = PageNumberPagination


class NewsItemApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsItemSerializer


class LawListApiView(generics.ListAPIView):
    queryset = Law.objects.all()
    serializer_class = LawListSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = LawFilter

class LawItemApiView(generics.RetrieveAPIView):
    queryset = Law.objects.all()
    serializer_class = LawItemSerializer
