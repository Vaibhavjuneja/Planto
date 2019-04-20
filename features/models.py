from django.db import models

# Create your models here.
class Disease(models.Model):
    dis_name = models.CharField(max_length=300,null=False,unique=True)
    dis_image = models.ImageField(upload_to='pictures/%Y/%m/%d/',max_length=500,blank=True)
    dis_symptoms = models.CharField(max_length=1000,null=False)


    def __str__(self):
        return self.dis_name



