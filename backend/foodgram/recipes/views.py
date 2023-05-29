from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from users.pagination import LimitPageNumberPagination

from .filters import AuthorAndTagFilter, IngredientNameFilter
from .models import Cart, Favorite, Ingredient, Recipe, RecipeIngredient, Tag
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import (FavoriteSerializers, IngredientSerializer,
                          RecipeSerializer, TagSerializer)


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    filterset_class = IngredientNameFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = LimitPageNumberPagination
    filter_class = AuthorAndTagFilter
    permission_classes = [IsOwnerOrReadOnly]

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_name="favorite",
        url_path="favorite",
        permission_classes=[IsAuthenticated],
        serializer_class=FavoriteSerializers
    )
    def favorite(self, request, pk=id):
        if request.method == 'POST':
            user = request.user
            recipe = self.get_object()
            if Favorite.objects.filter(user=user, recipe=recipe).exists():
                return Response({
                    'errors': 'Нельзя повторно добавить рецепт в избранное'
                }, status=status.HTTP_400_BAD_REQUEST)
            favorite = Favorite.objects.create(user=user, recipe=recipe)
            serializer = FavoriteSerializers(favorite)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            favorite = get_object_or_404(
                Favorite, user=request.user, recipe__id=pk
            )
            favorite.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_name="shopping_cart",
        url_path="shopping_cart",
        permission_classes=[IsAuthenticated],
        serializer_class=FavoriteSerializers
    )
    def shopping_cart(self, request, pk=id):
        if request.method == 'POST':
            user = request.user
            recipe = self.get_object()
            if Cart.objects.filter(user=user, recipe=recipe).exists():
                return Response({
                    'errors': 'Нельзя повторно добавить рецепт в корзину'
                }, status=status.HTTP_400_BAD_REQUEST)
            favorite = Cart.objects.create(user=user, recipe=recipe)
            serializer = FavoriteSerializers(favorite)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            favorite = get_object_or_404(
                Cart, user=request.user, recipe__id=pk
            )
            favorite.delete()
            return Response(
                f'Рецепт {favorite.recipe} удален из корзины у пользователя'
                f' {request.user}', status=status.HTTP_204_NO_CONTENT
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['GET'],
        url_name='download_shopping_cart',
        url_path='download_shopping_cart',
        permission_classes=[IsAuthenticated]
    )
    def download_shopping_cart(self, request):
        buying_list = {}
        user = request.user
        ingredients = RecipeIngredient.objects.filter(
            recipe__cart__user=user
        )
        for item in ingredients:
            amount = item.amount
            name = item.ingredient.name
            measurement_unit = item.ingredient.measurement_unit
            if name not in buying_list:
                buying_list[name] = {
                    'amount': amount,
                    'measurement_unit': measurement_unit
                }
            else:
                buying_list[name]['amount'] = (
                    buying_list[name]['amount'] + amount
                )
        shopping_list = []
        for item in buying_list:
            shopping_list.append(
                f'{item} - {buying_list[item]["amount"]}, '
                f'{buying_list[item]["measurement_unit"]}\n'
            )
        shopping_list_text = ''.join(shopping_list)
        response = HttpResponse(content_type='text/plain')
        response[
            'Content-Disposition'
        ] = 'attachment; filename="shopping_list.txt"'
        response.write(shopping_list_text)
        return response
