from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    # 전체 게시물 가져오는 코드
    articles = Article.objects.all()
    #소문자인데 articles라면 변수 여러개 데이터 가지고 있다
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


# create 버튼은 get
# submit 은 post
def create(request):
    # new/-> 빈종이를 보여주는기능
    # create/ 사용자가 입력한 데이터를 저장

    # GET --> create/ 빈 종이를 보여주는 기능
    # POST --> create/ 사용자가 입력한 데이터 저장


    if request.method == 'POST':  # 저장
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
        else:
            # form = ArticleForm()
            context = {
                'form': form,
            }
            return render(request, 'create.html', context)
    

    else:                           # 빈 종이 보여주는
        form = ArticleForm()

        context = {
            'form': form,
        }
        return render(request, 'create.html', context)
            
    