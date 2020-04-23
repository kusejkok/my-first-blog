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
    path('polls_list/', views.polls_list, name='polls_list'),
    path('polls_list/<int:question_id>/', views.polls_detail, name='polls_detail'),
    path('polls_list/<int:question_id>/vote/', views.polls_vote, name='polls_vote'),
    path('polls_list/<int:question_id>/results/', views.polls_results, name='polls_results'),
    path('python/', views.python_learning, name='python_learning'),
    path('python/python_blog', views.python_blog, name='python_blog'),
    path('python/python_blog/new/', views.python_blog_new, name='python_blog_new'),
    path('html/', views.html_learning, name='html_learning'),
    path('terminal/', views.terminal_learning, name='terminal_learning'),
    path('other/', views.other_learning, name='other_learning'),
    path('questions/', views.question_list, name = 'question_list'),
]
