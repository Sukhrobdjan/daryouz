from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from helpers.models import BaseModel
from common.models import User





LINKS = [
    ('DARYO', 'DARYO'),
    ('REKLAMA', 'REKLAMA'),
    ('IJTIMOIY TARMOQLAR','IJTIMOIY TARMOQLAR'),
    ('TELEGRAM-KANALLAR','TELEGRAM-KANALLAR'),
    ]


class Category(BaseModel):
    title = models.CharField(max_length=250,unique=True)
    slug = models.CharField(max_length=200,unique=True)
    post_count = models.IntegerField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title



class Post(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    img = models.ImageField(upload_to = 'post-img/')
    foto_auth = models.CharField(max_length=100)
    view_count = models.BigIntegerField(default=0)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Link(BaseModel):
    title = models.CharField(max_length=200,choices=LINKS)
    link = models.URLField()
    

    def __str__(self):
        return self.title
