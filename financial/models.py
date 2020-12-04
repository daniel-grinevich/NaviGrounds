from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

# Create your models here.
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.IntegerField(default=0)
    receipt_img = models.ImageField(upload_to='receipt_pics',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} Contribution'

    def get_absolute_url(self):
        return reverse('contrib-home')
