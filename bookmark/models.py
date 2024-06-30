from django.db import models

class Bookmark(models.Model):
    movie_name = models.CharField(max_length=100)
    review_text = models.TextField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_name
