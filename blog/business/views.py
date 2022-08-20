
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, get_list_or_404

from blog.utils.error_response import ErrorResponse

from business.models import Article
from business.serializers import ArticleSerializer,\
    ArticleDetailSerializer, ArticleListSerializer


class ArticleView(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        return Article.objects.all(*args, **kwargs)

    @action(detail=True, methods=['get'])
    def list(self, request):

        serializer = ArticleListSerializer(
            get_list_or_404(self.get_queryset()), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get(self, request, id):
        article = get_object_or_404(
            self.get_queryset(), id=id)
        serializer = ArticleDetailSerializer(instance=article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_serializer = ArticleDetailSerializer(
                instance=serializer.instance)

            return Response(
                new_serializer.data, status=status.HTTP_201_CREATED)
        return ErrorResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update(self, request, id):
        article = get_object_or_404(self.get_queryset(), id=id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_serializer = ArticleDetailSerializer(
                instance=serializer.instance)
            return Response(new_serializer.data, status=status.HTTP_200_OK)
        return ErrorResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, id):
        get_object_or_404(self.get_queryset(), id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
