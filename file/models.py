from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    logo = models.FileField()

    def __str__(self):
        return self.title +'-'+self.detail

class resume(models.Model):
    res_file = models.FileField()
