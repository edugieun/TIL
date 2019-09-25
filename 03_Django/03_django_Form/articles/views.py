from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    # articles = get_list_or_404(Article) 글이 하나도 없을 경우 에러 발생
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding)
        # 이 처리 과정은 binding 이라고 불리며, 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        # embed()
        # form 이 유효한지 체크한다.
        if form.is_valid():
            # form.cleaned_data 로 정제된 데이터를 받는다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.form(title=title, content=content)
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET : 기본 form
    # 2. POST : 검증에 실패 후의 form(is_valid == False)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


# def detail(request, article_pk):
#     try:
#         article = Article.objects.get(pk=article_pk)
#     except Article.DoesNotExist:
#         raise Http404('No Article matches the given query.')
#     context = {'article': article,}
#     return render(request, 'articles/detail.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)        
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            article = form.save()
            return redirect(article)
    else:
        # embed()
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        ##
        # ArticleForm 을 초기화(이전에 DB에 저장된 데이터를 넣어준 상태)
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        # form = ArticleForm(initial=article.__dict__)
        form = ArticleForm(instance=article)
    
    # 1. POST : 검증에 실패한 form(오류 메세지 포함 상태)
    # 2. GET : 초기화된 form
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)