from django.db import models

class Course(models.Model):
  Course_name = models.CharField(max_length=100)
  Course_info = models.TextField()

  def __str__(self):
    return self.Course_name