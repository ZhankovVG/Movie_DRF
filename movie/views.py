from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviwCreateSerializer


class MovieListView(APIView):
    # Movie list output
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

class MovieDetailView(APIView):
    # Full description
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    

class ReviewCreateView(APIView):
    # Movie review additions
    def post(self, request):
        review = ReviwCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)