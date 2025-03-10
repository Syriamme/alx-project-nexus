from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Pagination Class
class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()  # Optimized with select_related
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()  # Optimized with select_related
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

# Product List View with Pagination, Filtering, and Sorting
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.select_related('category').all()  # Optimize with select_related
        category = self.request.query_params.get('category')
        sort_by = self.request.query_params.get('sort_by')

        # Filter by category if provided
        if category:
            queryset = queryset.filter(category__name__icontains=category)

        # Sorting logic
        if sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')

        return queryset