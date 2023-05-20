from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    class Meta:
        permissions = (("can_view_feature_product", "View feature product"),)

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.CharField(max_length=100)
    #price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    image = models.ImageField(default='default.jpg', blank=True) # if picture is not uploaded, use this picture as default

    def __str__(self):
        return self.title

    def euro(self):
        return self.price + ' EUR'
