from rest_framework import generics

from .models import Movie
from .serializers import *
from .service import get_client_ip


class MovieListView(generics.ListAPIView):
    # Movie list output
    serializer_class = MovieListSerializer

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count('rating', filter=models.Q(rating__ip=get_client_ip(self.request)))
            ).annotate(
                middle_star=models.Sum(models.F('rating__star')) / models.Count(models.F('rating'))
            )
        return movies
    

class MovieDetailView(generics.RetrieveAPIView):
    # Full description
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer
    

class ReviewCreateView(generics.CreateAPIView):
    # Movie review additions
    serializer_class = ReviwCreateSerializer
    

class AddStarRatingView(generics.CreateAPIView):
    # Adding a rating to a movie
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))
        

class ActorListView(generics.ListAPIView):
    # list actors
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):
    # List of actors and directors
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer