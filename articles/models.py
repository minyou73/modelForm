from django.db import models

# Create your models here.
# 어떤 데이터 넣을지 정의하는 공간
# models.Model  장고에서 사용하는거 상속
class Artcicle(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    #만들어지는시간
    created_at = models.DateTimeField(auto_now_add=True)
    #수정시간
    updated_at = models.DateTimeField(auto_now=True)