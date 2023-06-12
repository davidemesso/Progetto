from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Route(models.Model):
    name = models.CharField(max_length = 180)
    difficulty = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(max_length = 500)
    end_date = models.DateField(null=True)
    image = models.ImageField(upload_to='route_images/')

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 1500)
    insert_date = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="favorites")