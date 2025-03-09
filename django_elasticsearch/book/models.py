
import uuid
from django.db import models


# Create your models here.
class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    image_link = models.SlugField()
    language = models.CharField(max_length=64)
    link = models.SlugField()
    pages = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=64)
    year = models.SmallIntegerField()

    def __str__(self):
        """Return a string representation of the product."""
        return str(self.title)
