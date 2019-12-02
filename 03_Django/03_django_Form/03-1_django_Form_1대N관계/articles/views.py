from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


# def delete(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     if request.method == 'POST':
#         article.delete()
#         return redirect('articles:index')
#     else:
#         return redirect(article)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) 
    comments = article.comment_set.all() # article의 모든 댓글
    comment_form = CommentForm() # 댓글 폼
    context = {'article': article, 'comment_form': comment_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)

@require_POST
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)

# def comments_create(request, article_pk):
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             # 바로 저장하기 전에 잠깐 멈춰야 article_pk를 가져올 수 있다.
#             # 객체를 create 하지만, db에 레코드를 저장하진 않는다.
#             comment = comment_form.save(commit=False)
#             comment.article_id = article_pk
#             comment.save()
#     return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)


# def comments_delete(request, article_pk, comment_pk):
#     if request.method == 'POST':
#         comment = get_object_or_404(Comment, pk=comment_pk)
#         comment.delete()
#     return redirect('articles:detail', article_pk)