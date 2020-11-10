from lessons import models

from django.contrib import admin


@admin.register(models.UserExtend)
class UserExtend(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('lesson',)


@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'type',)


@admin.register(models.Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question')


@admin.register(models.StudentResponses)
class StudentResponsesAdmin(admin.ModelAdmin):
    list_display = ('student',)

