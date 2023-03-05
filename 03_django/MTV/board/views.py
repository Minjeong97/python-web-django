from django.shortcuts import render, redirect
# 사용자의 요청에 대해 HTTP Response를 반환하기 위한 모듈
from django.http import HttpResponse
from .models import Posting

'''
# index() 함수, request를 파라미터로 받음(Django에 의해 자동으로 전달되는 HTTP 요청 객체)
def index(request):
    return HttpResponse("Main Board Page")  # 문자열을 사용자의 요청에 대한 응답으로 반환

from django.shortcuts import render, redirect
'''
# 글 목록 화면 (Read)
def index(request):
    # 글 목록 조회 
    # db article 관련된 레코드 전체를 조회
    postings = Posting.objects.all()  # QuerySet(List)
    context = {
        'postings': postings,
    }
    return render(request, 'board/index.html', context)

# 글 상세 화면 (Read)
def detail(request, posting_pk):
    # db > articles > 특정 레코드 조회
    # pk = request.GET.get('no')
    print(type(posting_pk))
    posting = Posting.objects.get(pk=posting_pk)  # primary key 가 1인 것을 객체로 가져옴.
    context = { 'posting': posting, }
    return render(request, 'board/detail.html', context)


# 글 쓰기 화면 (Creat)
def new(request):
    return render(request, 'posting/new.html')

# 글 실제 저장
def create(request):
    posting = Posting()
    posting.title = request.POST['title']
    posting.content = request.POST['content']
    posting.save()
    # hard redirect로 하는 방법
    # return redirect(f'/blog/{article.pk}/')  

    # detail 로 redirect 하자
    return redirect('board:index', posting.pk)

# 글 수정 화면 (Update)

def edit(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = { 'postings': posting, }
    return render(request, 'board/edit.html', context)

# 글 DB에  실제 수정 
def update(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    posting.title = request.POST['title']
    posting.content = request.POST['content']
    posting.save()
    # 저장하고 detail로 redirect 하자!
    return redirect('board:detail', posting_pk.pk)

# 글 삭제 ?? (Delete)
def delete(request, posting_pk):
    if request.method == 'POST':
        # 특정 게시글을 지운다.
        # 1. 고른다.
        posting = Posting.objects.get(pk=posting_pk)
        # 2. 지운다.
        posting.delete()
    return redirect('board:index')
    