from django_filters import rest_framework as filters
from movie.models import Movie
from rest_framework.pagination import PageNumberPagination


def get_client_ip(request):
        # User api retrieval
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR') 
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ['genres', 'year']


class PaginationMovies(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 1000