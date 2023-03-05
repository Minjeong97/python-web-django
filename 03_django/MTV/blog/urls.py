# mtv/urls.py (master URL)

from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # blog/
    path('', views.index, name='index'),
    # blog/1 (detail)/
    path('<int:article_pk>/', views.detail, name='detail'),
    # blog/new/
    path('new/', views.new, name='new'),
    # blog/create/
    path('create/', views.create, name='create'),
    # blog/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # blog/update
    path('<int:article_pk>/update/', views.update, name='update'),
    # blog/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),

]


'''
URL => 내 맘대로
1. Resource 를 표현
2. 명사형
3. 확실히 구분
4. (동사는 빼라)
'''
