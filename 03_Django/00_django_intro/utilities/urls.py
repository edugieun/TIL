from django.urls import path
from . import views # 마침표 (.)는 현재 위치(폴더)라는 의미

urlpatterns = [
    path('index/', views.index),
]