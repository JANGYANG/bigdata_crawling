from django.db import models
from django.utils import timezone


class Community(models.Model):
    #cName=커뮤니티이름
    cName = models.CharField(max_length=100)
    #tname=게시판이름
    tName = models.CharField(max_length=100)
    conType = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date = models.DateTimeField(
            blank=True, null=True)


    def __str__(self):
        return self.content