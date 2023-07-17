from django import forms
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Category
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {"url" : ("name",)}


class ReviewInline(admin.StackedInline):
    # Attaching movie reviews
    model = Review
    readonly_fields = ('name', 'email')
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Movie
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', )
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    list_editable = ('draft',)
    prepopulated_fields = {"url" : ("title",)}


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    # Review
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')
    list_display_links = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Genre
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {"url" : ("name",)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # Actor
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='50' ")
    
    get_image.short_description = 'Изображение'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    # Frames from the movie
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.imege.url} width='50' height='50' ")
    
    get_image.short_description = 'Изображение'


@admin.register(Reting)
class RetingAdmin(admin.ModelAdmin):
    # Reting
    list_display = ('ip', 'star')


admin.site.register(RatingsStar)
