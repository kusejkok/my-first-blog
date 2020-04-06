from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
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
        ('Easy', 'Eays'),
        ('Doable', 'Doable'),
        ('Difficult', 'Difficult'),
        ('Very difficult', 'Very difficult'),
    ]
    difficulty = models.CharField(max_length = 10, choices = DIFF, default = 'Doable')
    learned = models.BooleanField(default = 'False')
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
