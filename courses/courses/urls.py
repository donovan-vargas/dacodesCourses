from lessons import views

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CoursesViewSet)
router.register('lessons', views.LessonsViewSet)
router.register('questions', views.QuestionsViewSet)
router.register('answers', views.AnswersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
