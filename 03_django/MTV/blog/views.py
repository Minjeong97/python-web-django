from django.shortcuts import render, redirect
from .models import Article

# 글 목록 화면 (Read)
def index(request):
    # 글 목록 조회 
    # db article 관련된 레코드 전체를 조회
    articles = Article.objects.all()  # QuerySet(List)
    context = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)

# 글 상세 화면 (Read)
def detail(request, article_pk):
    # db > articles > 특정 레코드 조회
    # pk = request.GET.get('no')
    print(type(article_pk))
    article = Article.objects.get(pk=article_pk)  # primary key 가 1인 것을 객체로 가져옴.
    context = { 'article': article, }
    return render(request, 'blog/detatil.html', context)


# 글 쓰기 화면 (Creat)
def new(request):
    return render(request, 'blog/new.html')

# 글 실제 저장
def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    # hard redirect로 하는 방법
    # return redirect(f'/blog/{article.pk}/')  

    # detail 로 redirect 하자
    return redirect('blog:index', article.pk)

# 글 수정 화면 (Update)

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = { 'article': article, }
    return render(request, 'blog/edit.html', context)

# 글 DB에  실제 수정
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    # 저장하고 detail로 redirect 하자!
    return redirect('blog:detail', article.pk)

# 글 삭제 ?? (Delete)
def delete(request, article_pk):
    if request.method == 'POST':
        # 특정 게시글을 지운다.
        # 1. 고른다.
        article = Article.objects.get(pk=article_pk)
        # 2. 지운다.
        article.delete()
    return redirect('blog:index')
    