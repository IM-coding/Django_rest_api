from rest_framework import serializers
from libapp.models import Book, Opinion

# serializer for opinion model
class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['rating', 'description']

# serializer for book model
class BookSerializer(serializers.ModelSerializer):

    # connecting 2 models to recieve all data with search
    opinions = OpinionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'book_type', 'opinions']