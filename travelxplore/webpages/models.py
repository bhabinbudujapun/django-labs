from django.db import models

# Create your models here.


class Destination(models.Model):
    d_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='d_id')
    d_name = models.CharField(max_length=50)
    d_img = models.ImageField(upload_to='images')
    d_desc = models.TextField()
    d_price = models.IntegerField()
    d_offer = models.BooleanField(default=False)
