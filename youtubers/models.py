from email.policy import default
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):
    crew_choices=(
        ('solo','solo'),
        ('small','samll'),
        ('large','large')
    )
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url=models.CharField(max_length=255)
    Description=RichTextField()
    age=models.IntegerField()
    height=models.IntegerField()
    crew=models.CharField(choices=crew_choices,max_length=255)
    camera=models.CharField(max_length=255)
    subs_count=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    is_featured=models.BooleanField(default=False)
    created_data=models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.name
    
