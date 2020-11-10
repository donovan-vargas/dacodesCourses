from lessons import models
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication


class EverybodyCanAuthentication(SessionAuthentication):
    def authenticate(self, request):
        return None


class UserExtendSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserExtend
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Courses
        fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    course = CoursesSerializer(read_only=True)

    class Meta:
        model = models.Lessons
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer(read_only=True)

    class Meta:
        model = models.Questions
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    question = QuestionsSerializer(read_only=True)

    class Meta:
        model = models.Answers
        fields = '__all__'