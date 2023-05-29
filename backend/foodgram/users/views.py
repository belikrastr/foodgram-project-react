from djoser.views import UserViewSet as DjoserViewSet
from recipes.serializers import FollowSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Follow, User
from .pagination import LimitPageNumberPagination


class CustomUserViewset(DjoserViewSet):
    pagination_class = LimitPageNumberPagination

    @action(
        detail=False,
        methods=['GET'],
        url_name="me",
        url_path="me",
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['GET'],
        url_name="subscriptions",
        url_path="subscriptions",
        permission_classes=[IsAuthenticated]
    )
    def subscriptions(self, request):
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_name="subscribe",
        url_path="subscribe",
        permission_classes=[IsAuthenticated]
    )
    def subscribe(self, request, id=None):
        if request.method == 'POST':
            user = request.user
            author = get_object_or_404(User, id=id)
            if user == author:
                return Response({
                    'errors': 'Вы не можете подписываться на самого себя'
                }, status=status.HTTP_400_BAD_REQUEST)
            if Follow.objects.filter(user=user, author=author).exists():
                return Response({
                    'errors': 'Вы уже подписаны на данного пользователя'
                }, status=status.HTTP_400_BAD_REQUEST)
            follow = Follow.objects.create(user=user, author=author)
            serializer = FollowSerializer(
                follow, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            user = request.user
            author = get_object_or_404(User, id=id)
            if user == author:
                return Response({
                    'errors': 'Вы не можете отписаться от самого себя'
                })
            follow = Follow.objects.filter(user=user, author=author)
            if follow.exists():
                follow.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                serializer.data, {
                    'errors': 'Вы не можете отписаться от автора, на которого'
                    ' не подписаны. Подпишитесь на него - он классный повар!'
                }
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
