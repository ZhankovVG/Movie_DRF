from rest_framework import serializers
from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    # list movie
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'category')


class MovieDetailSerializer(serializers.ModelSerializer):
    # full description
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Movie
        exclude = ('draft', )