from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors ['name'] = "Name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors ['description'] = "Description should be at least 15 characters"
        return errors

class CommentManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "Comment must be at least 5 characters"
        return errors

class Course(models.Model):
    name=models.CharField(max_length=45)
    description=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="has_comments",on_delete=models.CASCADE)

    objects = CommentManager()

