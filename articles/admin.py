from django.contrib import admin
from .models import Article
# Register your models here.
# article 페이지 admin에 등록 후 확인

admin.site.register(Article)