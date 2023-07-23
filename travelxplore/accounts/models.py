from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# class User(AbstractUser):
#     # Your custom fields go here
#     contact_number = models.CharField(max_length=15, blank=True, null=True)

#     # Fix reverse accessor clash for groups field
#     groups = models.ManyToManyField(Group, related_name='user_accounts')

#     # Fix reverse accessor clash for user_permissions field
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='user_accounts')

# class Destination(models.Model):
#     d_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='d_id')
#     d_name = models.CharField(max_length=50)
#     d_img = models.ImageField(upload_to='images')
#     d_desc = models.TextField()
#     d_price = models.IntegerField()
#     d_offer = models.BooleanField(default=False)
