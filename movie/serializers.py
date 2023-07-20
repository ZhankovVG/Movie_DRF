from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    # list movie
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'tagline', 'category', 'rating_user', 'middle_star')


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


class ActorListSerializer(serializers.ModelSerializer):
    # The output of directors and actors
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class ActorDetailSerializer(serializers.ModelSerializer):
    # Full description
    class Meta:
        model = Actor
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    # full description
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = ActorListSerializer(read_only=True, many=True)
    actors = ActorListSerializer(read_only=True, many=True)
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
    
