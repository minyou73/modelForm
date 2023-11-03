from django.apps import AppConfig

# article 페이지 admin에 등록 후 확인
class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
