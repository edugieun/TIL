from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # 아래처럼 문자열을 변수로 받는 경우는 맨 아래 순서로 내려야한다.
    # 안그러면 모든 페이지 (signup, login 등)를 문자열로 인식하여 views.profile로 보내버린다.
    path('<username>/', views.profile, name='profile'), 
]
