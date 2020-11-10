from lessons import serializers, models

import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework import viewsets, views, filters, status


class CoursesViewSet(viewsets.ModelViewSet):
    """
    Courses viewset
    methods: GET, POST, PUT, DELETE
    """
    queryset = models.Courses.objects.filter(active=True)
    serializer_class = serializers.CoursesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['favorite', 'course_number']

    def create(self, request, *args, **kwargs):
        serializer = request.data
        professor = request.user.user_extend.get().is_professor
        if not professor:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        courses = request.user.instructor.count()
        name = serializer.get('name')
        description = serializer.get('description')
        course_number = courses + 1
        instructor = request.user
        obj, created = models.Courses.objects.get_or_create(
            name=name,
            description=description,
            course_number=course_number,
            instructor=instructor
        )
        if created:
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        course = self.get_object()
        course.active = False
        course.save()
        return Response({"status": "deactivate"})


class LessonsViewSet(viewsets.ModelViewSet):
    """
    Lessons viewset
    methods: GET, POST, PUT, DELETE
    GET: by course id: course_id query parameter
    """
    queryset = models.Lessons.objects.filter(active=True)
    serializer_class = serializers.LessonsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['lesson']
    ordering_fields = ['lesson_number']

    def get_queryset(self):
        course = self.request.query_params.get('course_id', None)
        if course is not None:
            return models.Lessons.objects.filter(course=course)
        return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = request.data
        professor = request.user.user_extend.get().is_professor
        if not professor:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        course = serializer.get('course')
        lesson_number = models.Lessons.objects.filter(course=course).count() + 1
        course = models.Courses.objects.get(pk=course)
        lesson = serializer.get('lesson')
        description = serializer.get('description')
        approval_score = serializer.get('approval_score')
        obj, created = models.Lessons.objects.get_or_create(
            course=course,
            lesson=lesson,
            description=description,
            lesson_number=lesson_number,
            approval_score=approval_score,
        )
        if created:
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        lesson = self.get_object()
        lesson.active = False
        lesson.save()
        return Response({"status": "deactivate"})


class QuestionsViewSet(viewsets.ModelViewSet):
    """
    Questions viewset
    methods: GET, POST, PUT, DELETE
    """
    queryset = models.Questions.objects.filter(active=True)
    serializer_class = serializers.QuestionsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['question']
    ordering_fields = ['score', 'type']

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        question.active = False
        question.save()
        return Response({"status": "deactivate"})


class AnswersViewSet(viewsets.ModelViewSet):
    """
    Answers viewset
    methods: GET, POST, PUT, DELETE
    GET: by lesson id: lesson_id query parameter
    """
    queryset = models.Answers.objects.filter(active=True)
    serializer_class = serializers.AnswersSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['answer']
    ordering_fields = ['is_correct']

    def get_queryset(self):
        lesson = self.request.query_params.get('lesson_id', None)
        if lesson is not None:
            return models.Answers.objects.filter(question__lesson=lesson)
        return self.queryset

    def destroy(self, request, *args, **kwargs):
        answer = self.get_object()
        answer.active = False
        answer.save()
        return Response({"status": "deactivate"})
