from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.username}"


class Task(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default="")