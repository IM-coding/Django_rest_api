from libapp.models import Book
from libapp.serializers import BookSerializer
from rest_framework import generics
from rest_framework import filters

class LibraryAPIView(generics.ListAPIView):
    """
    API endpoint that allows users to be view and search.
    """
    
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'slug']
    queryset = Book.objects.all()


    #TODO: custom template with search form.