from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Article
from .serilaizer import ArticleSerializer
from paginations import CustomArticlePagination


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class ArticleListView(generics.ListAPIView):
    # pagination_class = ArticlePagination
    pagination_class = CustomArticlePagination
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(is_published = True).order_by('-created_at')
    
