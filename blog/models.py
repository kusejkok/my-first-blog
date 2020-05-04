from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    IT_NEW = [
        ('DJANGO', 'Django'),
        ('PYTHON', 'Python'),
        ('HTML', 'html'),
        ('SQL', 'sql'),
        ('CSS', 'css'),
        ('GIT', 'git'),
        ('OTHER', 'other')
    ]
    subtitle = models.CharField(max_length = 10, choices = IT_NEW, default = 'DJANGO')
    DIFF = [
        ('Easy', 'Easy'),
        ('Doable', 'Doable'),
        ('Difficult', 'Difficult'),
        ('Very difficult', 'Very difficult'),
    ]
    difficulty = models.CharField(max_length = 14, choices = DIFF, default = 'Doable')
    learned = models.BooleanField(default = 'False')
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PollsQuestion(models.Model):
    polls_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.polls_text

class PollsChoices(models.Model):
    question_id = models.ForeignKey(PollsQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text


class Question(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    urgent = models.BooleanField(default = 'False')
    created_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PythonExample(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class VisitorsInfo(models.Model):
    name = models.CharField(max_length = 50)
    knowDjango = models.BooleanField(default = "False")
    skillsDjango = models.IntegerField(default = 0)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
