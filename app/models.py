from django.db import models

# Create your models here.
class SchoolInfo(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)

    def __str__(self):
        return self.name