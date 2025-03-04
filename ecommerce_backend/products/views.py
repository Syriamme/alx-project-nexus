from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        sort_by = self.request.query_params.get('sort_by')

        if category:
            queryset = queryset.filter(category__name=category)

        if sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')

        return queryset

