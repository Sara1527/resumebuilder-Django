from django.db import models

# Create your models here.
class Resume(models.Model):
    banner = models.ImageField(upload_to="images/",default="")
    name = models.CharField(max_length=60,unique="True")
    phone = models.IntegerField()
    summary = models.TextField(max_length=200,default="")
    email = models.EmailField(max_length=200,unique="True")
    education = models.TextField(max_length=200,default="")
    experience = models.TextField(default="")
    Skills = models.TextField(default="")
    hobbies = models.TextField(max_length=100,default="")
    references = models.TextField(max_length=200,default="")

    def __str__(self):
        return self.name

