from django.db import models

class Item(models.Model):
    name = models.CharField( max_length=50)
    detail = models.CharField(max_length=200)
    image=models.ImageField(upload_to="media/")


    def __str__(self):
        return f"{self.name} "