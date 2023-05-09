from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return self.text

    def euro(self):
        return self.price + " EUR"
