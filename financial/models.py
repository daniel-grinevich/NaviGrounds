from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Status(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}'

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    receipt_img = models.FileField(default='default.jpg', upload_to='receipt_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    TYPE_CHOICES = (
        ("Contribution", "Contribution"),
        ("Personal Expense","Personal Expense"),
        ("Company Expense", "Company Expense"),
        ("Invoice", "Invoice")
    )
    type = models.CharField(max_length=22,
                  choices=TYPE_CHOICES,
                  default="Contribution")
    time_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    STATUS_CHOICES = (
        ("COMPLETE", "Complete"),
        ("INCOMPLETE","Incomplete")
    )
    status = models.CharField(max_length=10,
                  choices=STATUS_CHOICES,
                  default="INCOMPLETE")

    def __str__(self):
        return f'{self.id} Contribution'

    def get_absolute_url(self):
        return reverse('contrib-home')
