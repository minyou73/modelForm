from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    # 전체 게시물 가져오는 코드
    articles = Article.objects.all()
    #소문자인데 articles라면 변수 여러개 데이터 가지고 있다
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

    