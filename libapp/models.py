from django.template.defaultfilters import slugify
from django.db import models

# Book database model for all books in library
class Book(models.Model):
    # Unique field for book number to prevent duplicates, index for quicker search 
    isbn = models.IntegerField(
        unique=True,
        db_index=True,
    )
    title = models.TextField()
    author = models.TextField(
        null=True,
        blank=True,
    )
    book_type = models.TextField(
        null=True,
        blank=True,
    )
    # Slug field for filtering against url with get request
    slug = models.SlugField(
        null=True, 
        blank=True,
        db_index=True,
    )

    # For testing
    def __str__(self):
        return f'{self.isbn}: {self.title} --- {self.author}'

    # Slugify book title when save
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Book, self).save(*args, **kwargs)

# Opinion database model for all opinions with foreign key to book
class Opinion(models.Model):

    # Foreign key to make 2 small connected tables.
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='opinions',
    )
    rating = models.IntegerField()
    description = models.TextField(
        null=True,
        blank=True,
    )

    # For testing
    def __str__(self):
        return self.description