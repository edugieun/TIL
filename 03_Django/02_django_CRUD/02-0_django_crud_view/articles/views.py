from IPython import embed # pip install ipython로 먼저 설치해야 쓸 수 있음
from django.core.exceptions import ValidationError # 장고 에러 객체
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()

    # 뒤집어서(최신순으로) 보내는 2가지 방법
    # 파이썬의 경우 한번 더 불러야 하므로 느릴 수도 있음
    articles = Article.objects.order_by('-pk') # 1. ORM, DB가 변경
    # articles = Article.objects.all()[::-1] # 2. python이 변경

    context = {'articles': articles,}

    return render(request, 'articles/index.html', context)


# CRUD에서 C(create)를 담당하는 애들
# 1. new
# 2. create
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    try: # 유효성 검사
        # embed() # 서버 일시정시
        # title = request.GET.get('title')
        # content = request.GET.get('content')
        # POST 방식
        title = request.POST.get('title')
        content = request.POST.get('content')
        

        # 저장방법 1
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save() # save()해줘야 데이터베이스로 들어감

        # 저장방법2 : 간결하면서 유효성 검사도 가능
        article = Article(title=title, content=content)

        # 유효성 검사
        # 나중에는 is_valid() 와 같은 메서드를 쓸거임.
        article.full_clean()
    except ValidationError:
        raise ValidationError('Error')
    else:
        article.save()
    
    
        # 저장방법3
        # Article.objects.create(title=title, content=content)

        # return render(request, 'articles/index.html') 
        # 이렇게 하면 index로 갈 수 있나? 그렇지 않다.
        # 페이지는 index를 보여주지만, url 값은 여전히 create이다.
        
        # redirect를 이용하여 url을 통한 페이지 전환이 가능하다.
        # redirect 를 쓰면 create.html은 필요없게 된다.
        # return redirect('/articles/')

        # 글 작성후 바로 detail로 들어가기
        return redirect(f'/articles/{article.pk}/')

def detail(request, pk):
    # pk를 이용하여 하나의 게시글만 가져오기
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)

# DELETE

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')


# UPDATE
# 1. 수정하는 페이지 view(edit)
# 2. 직접 모델에 수정 요청을 보내는 view(update)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')