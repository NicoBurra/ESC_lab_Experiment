from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=50, unique=True)
    required_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, through='Enrollment')

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    hours_completed = models.FloatField(default=0)

    class Meta:
        unique_together = ('student', 'course')


class Experiment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.FloatField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Participation(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'experiment')
