from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 생성 시, 자동으로 채워지도록
    created_at = models.DateTimeField(auto_now_add=True)
    # 생성/수정 시, 자동으로 채워지도록
    updated_at = models.DateTimeField(auto_now=True)