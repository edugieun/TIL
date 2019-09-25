from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions}
    return render(request, 'eithers/index.html', context)


def create(request):
    # CREATE
    if request.method == 'POST':        
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect(question)
    # NEW
    else:
        return render(request, 'eithers/create.html')



def detail(request, question_pk):

    # 1번 방법
    # prefetch_related는 미리 'answer_set'를 가져옴으로써 나중에 쿼리를 다시 돌 필요가 없다. -> 쿼리의 성능 향상 및 최적화
    # question = Question.objects.prefetch_related('answer_set').get(pk=question_pk)
    question = Question.objects.get(pk=question_pk) 
    count_a = len(question.answer_set.filter(pick=0))
    count_b = len(question.answer_set.filter(pick=1))

    sum_ab = count_a + count_b
    
    if sum_ab == 0:
        a_per = 0
        b_per = 0
    else:
        a_per = round(count_a / sum_ab * 100, 2)
        b_per = round(count_b / sum_ab * 100, 2)

    context = {'question': question, 'a_per': a_per, 'a_per': a_per}
    return render(request, 'eithers/detail.html', context)

    # 2번 방법은 선생님 코드 참고 


def answers_create(request, question_pk):
    
    for answer in answers:

    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        pick = request.POST.get('pick')
        answer = Answer(question=question, comment=comment, pick=pick)
        answer.save()
        return redirect(question)
    else:
        return redirect(question)



# 랜덤 정렬 방법
# question = Question.objects.order_by('?')[0]