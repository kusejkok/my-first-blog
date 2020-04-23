from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Question, PythonExample, PollsQuestion, PollsChoices
from .forms import PostForm, PythonExampleForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'blog/base.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'blog/question_list.html', {'questions': questions})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

#@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

#@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')





def polls_list(request):
    pollsquestions = PollsQuestion.objects.all()
    return render(request, 'blog/polls_list.html', {'pollsquestions': pollsquestions})

def polls_detail(request, question_id):
    pollsquestion = get_object_or_404(PollsQuestion, pk = question_id)
    return render(request, 'blog/polls_detail.html', {'pollsquestion': pollsquestion})

def polls_vote(request, question_id):
    pollsquestion = get_object_or_404(PollsQuestion, pk=question_id)
    try:
        selected_choice = pollsquestion.pollschoices_set.get(pk=request.POST['choice'])
    except (KeyError, PollsChoices.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/polls_detail.html', {
            'pollsquestion': pollsquestion,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'blog/polls_results.html', {'pollsquestion': pollsquestion})

def polls_results(request, question_id):
    pollsquestion = get_object_or_404(PollsQuestion, pk=question_id)
    return render(request, 'blog/polls_results.html', {'pollsquestion': pollsquestion})

def python_learning(request):
    return render(request, 'blog/python_learning.html', {})

def python_blog(request):
    pythonexamples = PythonExample.objects.all()
    return render(request, 'blog/python_blog.html', {'pythonexamples': pythonexamples})

def python_blog_new(request):
    if request.method == "POST":
        form = PythonExampleForm(request.POST)
        if form.is_valid():
            pythonexample = form.save()
            pythonexample.save()
            return redirect('python_blog')
    else:
        form = PythonExampleForm()
    return render(request, 'blog/python_blog_new.html', {'form': form})


def html_learning(request):
    return render(request, 'blog/html_learning.html', {})

def terminal_learning(request):
    return render(request, 'blog/terminal_learning.html', {})

def other_learning(request):
    return render(request, 'blog/other_learning.html', {})
