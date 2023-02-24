from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=10)


    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return self.size

class Product(models.Model):
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    # size = models.ManyToManyField(Size)
    # color = models.ManyToManyField(Color)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'









