from django.conf import settings
from django.db import models
from django.utils import timezone

class Course_book(models.Model):
    author = models.CharField(max_length=50)
    book_title = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)
    material_id = models.PositiveIntegerField(primary_key=True )
    course_id = models.ForeignKey('Course',
        on_delete=models.CASCADE,)
    link_to_download = models.CharField(max_length=500)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book_title


class Course(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    course_id = models.PositiveIntegerField(primary_key=True)
    course_name = models.CharField(max_length=50)
    season = models.CharField(max_length=3)
    course_info = models.TextField(default='-')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.course_name
