from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_description = models.TextField(max_length=200)
    completed = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Images', default='Images/None/No-img.jpg')
    document = models.FileField(upload_to='Doc/', default='Doc/None/None-doc.pdf')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.task_name
