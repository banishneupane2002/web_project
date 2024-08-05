from django.db import models

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    country = models.CharField(max_length=50)
    message = models.TextField()
    newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.name