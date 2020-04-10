from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('achievedTasks/', views.post_list, name = 'post_list'),
    path('achievedTasks/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('achievedTasks/post/new/', views.post_new, name='post_new'),
    path('achievedTasks/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('achievedTasks/post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('achievedTasks/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('achievedTasks/drafts/', views.post_draft_list, name='post_draft_list'),
    path('python/', views.python_learning, name='python_learning'),
    path('html/', views.html_learning, name='html_learning'),
    path('terminal/', views.terminal_learning, name='terminal_learning'),
    path('other/', views.other_learning, name='other_learning'),
    path('questions/', views.question_list, name = 'question_list'),
]
