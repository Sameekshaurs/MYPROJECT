from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.email: #Automatically generate email if not provided
            self.email = f"{self.name.lower().replace(' ','.')}@example.com"
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Create your models here.
