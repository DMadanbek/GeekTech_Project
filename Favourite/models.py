from django.db import models
from Project.models import  Law
from rest_framework.authtoken.admin import User

class Favourite(models.Model):
    izb = models.ForeignKey(Law, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = "Избранное законов "

    def __str__(self):
        return self.izb.title
