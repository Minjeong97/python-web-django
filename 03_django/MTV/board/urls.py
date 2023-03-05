from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # blog/
    path('', views.index, name='index'),
    # blog/1 (detail)/
    path('<int:posting_pk>/', views.detail, name='detail'),
    # blog/new/
    path('new/', views.new, name='new'),
    # blog/create/
    path('create/', views.create, name='create'),
    # blog/edit/
    path('<int:posting_pk>/edit/', views.edit, name='edit'),
    # blog/update
    path('<int:posting_pk>/update/', views.update, name='update'),
    # blog/delete/
    path('<int:posting_pk>/delete/', views.delete, name='delete'),

]
