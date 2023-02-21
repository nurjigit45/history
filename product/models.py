from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Review(models.Model):
    text = models.TextField()
    raiting = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'коментария'
        verbose_name_plural = 'коментарии'




