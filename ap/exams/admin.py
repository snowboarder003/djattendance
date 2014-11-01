from django.contrib import admin
from exams.models import ExamTemplate, Exam, TextQuestion, TextResponse

# admin.site.register(TextQuestion)
# admin.site.register(TextResponse)
admin.site.register(Exam)

class TextQuestionInline(admin.StackedInline):
    model = TextQuestion
    extra = 1

class ExamTemplateAdmin(admin.ModelAdmin):
    inlines = [TextQuestionInline]

admin.site.register(ExamTemplate, ExamTemplateAdmin)