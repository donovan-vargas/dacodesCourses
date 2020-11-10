from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserExtend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_extend', verbose_name='usuario')
    phone = models.CharField(max_length=15, verbose_name='telefono')
    is_professor = models.BooleanField(default=False, verbose_name='es profesor')
    created = models.DateField(auto_now_add=True, verbose_name='creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='modificado')
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta(object):
        verbose_name_plural = 'Perfil usuario'

    def __str__(self):
        return self.user


class Courses(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    description = models.TextField(max_length=1024, verbose_name='descripcion')
    course_number = models.IntegerField()
    instructor = models.ForeignKey(User, related_name='instructor', on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(User, verbose_name='estudiantes')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='modificado')
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta(object):
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name


class Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    lesson = models.CharField(max_length=200, verbose_name='leccion')
    description = models.TextField(max_length=1024, verbose_name='descripcion')
    lesson_number = models.IntegerField()
    approval_score = models.DecimalField(decimal_places=2, max_digits=5)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='modificado')
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta(object):
        verbose_name_plural = 'Lecciones'

    def __str__(self):
        return self.lesson


class Questions(models.Model):
    TYPES = (
        ('boolean', 'boolean'),
        ('multiple', 'multiple'),
        ('multiple_more_than_ones', 'multiple_more_than_ones'),
        ('multiple_more_than_ones_all', 'multiple_more_than_ones_all'),
    )
    lesson = models.ForeignKey(Lessons, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=300, verbose_name='pregunta')
    score = models.IntegerField()
    type = models.CharField(max_length=200, choices=TYPES, default='boolean')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='modificado')
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta(object):
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='modificado')
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta(object):
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return self.answer


class StudentResponses(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answers, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='modificado')
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta(object):
        verbose_name_plural = 'Respuestas de estudiantes'

    def __str__(self):
        return self.student


