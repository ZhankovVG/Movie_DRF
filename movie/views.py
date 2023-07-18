from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import *


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
    

class AddStarRatingView(APIView):
    # Adding a rating to a movie
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR') 
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=self.get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)