from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def upload_to(instance, filename):
    return f'{filename}'


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    publication_date = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=1000)
    full_description = models.TextField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title


class ImageNews(models.Model):
    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='images')

    def __str__(self):
        return self.news.title


# class Law(models.Model):
# law = models.

class FavouriteNews(models.Model):
    product = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


class Law(models.Model):

    LAWS = [
        (1, 'Type 1'),
        (2, 'Type 2'),
        (3, 'Type 3'),
    ]
    title = models.CharField(max_length=200)
    types = models.CharField(max_length=30, choices=LAWS,default=True)
    short_description = models.CharField(max_length=1000)
    full_description = models.TextField()

    def __str__(self):
        return self.title

# types_two = models.IntegerField(max_length=30,choices=LAW,null=True)
# types_three = models.IntegerField(max_length=30,choices=LAWU,null=True)
