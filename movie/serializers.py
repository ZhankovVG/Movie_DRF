from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    # list movie
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'category')


class ReviwCreateSerializer(serializers.ModelSerializer):
    # adding a review

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    # output a reviews
    class Meta:
        model = Review
        fields = ('name', 'text', 'parent')


class MovieDetailSerializer(serializers.ModelSerializer):
    # full description
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ('draft', )


class CreateRatingSerializer(serializers.ModelSerializer):
    # add user rating
    class Meta:
        model = Reting 
        fields = ('star', 'movie')

    def create(self, validated_data):
        rating = Reting.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star')}
        )
        return rating
    