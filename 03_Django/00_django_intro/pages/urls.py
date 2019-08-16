from django.urls import path
from . import views # 마침표 (.)는 현재 위치(폴더)라는 의미

urlpatterns = [
    # 다른건 다 위로 쌓는데 app내부의 urls만 아래로 쌓음. 장고가 그렇게 하라고 함.
    path('index/', views.index), # url 경로 마지막에 / 를 붙이는 습관
    path('introduce/<name>/<age>', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<name>', views.hello),
    path('times/<int:num1>/<int:num2>', views.times),
    path('area/<int:r>', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]