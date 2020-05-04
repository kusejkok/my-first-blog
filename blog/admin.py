from django.contrib import admin
from .models import Post, Question, PythonExample, PollsQuestion, PollsChoices, VisitorsInfo


# Register your models here.
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(PythonExample)

class PollsChoicesInline(admin.TabularInline):
    model = PollsChoices
    extra = 3

class PollsQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['polls_text']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [PollsChoicesInline]

admin.site.register(PollsQuestion, PollsQuestionAdmin)
admin.site.register(PollsChoices)
admin.site.register(VisitorsInfo)
