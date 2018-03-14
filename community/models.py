import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models
from django.utils import timezone


class Community(models.Model):
    cName = models.CharField(max_length=100)
    tName = models.CharField(max_length=100)
    conType = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date = models.DateField(
            blank=True, null=True)


    def __str__(self):
        return self.content
        
        
class Test(models.Model):
    cName = models.CharField(max_length=100)
    tName = models.CharField(max_length=100)
    conType = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date = models.DateField(
            blank=True, null=True)


    def __str__(self):
        return self.content