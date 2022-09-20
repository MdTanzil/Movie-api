from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genres(models.Model):
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.genre


class Movie(models.Model):
        """Movie Class contain all of information about movies """
        
            # TODO: Create Table field

        title = models.CharField(blank = True,null = True, max_length=50)
        rating = models.IntegerField(
            default=1,
            validators=[
                MaxValueValidator(10),
                MinValueValidator(1)
            ])
        duration = models.DurationField(null=True)
        release_date = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
        genre=models.ManyToManyField(Genres)
        create_at = models.DateTimeField( auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title


