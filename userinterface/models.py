from django.db import models

# Create your models here.
class reviewcontact(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return '%s %s' % (self.first, self.last)


class myuploadfile(models.Model):
    fName = models.CharField(max_length=255)
    myFile = models.FileField(upload_to="")

    def __str__(self):
        return self.fName
    

