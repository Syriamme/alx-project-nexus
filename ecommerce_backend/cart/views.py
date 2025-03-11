from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart, Product
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class CartListView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class AddToCartView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=request.data.get('product_id'))
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity += int(request.data.get('quantity', 1))
        cart_item.save()
        return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_200_OK)

class RemoveFromCartView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=request.data.get('product_id'))
        cart_item = get_object_or_404(Cart, user=request.user, product=product)
        cart_item.delete()
        return Response({'message': 'Product removed from cart successfully'}, status=status.HTTP_200_OK)