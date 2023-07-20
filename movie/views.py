from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import *
from .service import get_client_ip


class MovieListView(APIView):
    # Movie list output
    def get(self, request):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count('rating', filter=models.Q(rating__ip=get_client_ip(request)))
            ).annotate(
                middle_star=models.Sum(models.F('rating__star')) / models.Count(models.F('rating'))
            )
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
    

class AddStarRatingView(APIView):
    # Adding a rating to a movie
    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)