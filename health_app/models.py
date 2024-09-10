from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)  # Add age field
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        null=True, 
        blank=True
    )  # Add gender field

class Symptom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.name

class UserSymptomReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.user.username} at {self.timestamp}"

class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name
    

    from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()  # URL of the article
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # Path to the image file

    def __str__(self):
        return self.title

from django.db import models

class Conversation(models.Model):
    disease = models.CharField(max_length=100)
    context = models.TextField()
    global_id = models.IntegerField(unique=True, blank=True, null=True)

    @classmethod
    def get_next_global_id(cls):
        max_global_id = cls.objects.aggregate(max_id=models.Max('global_id'))['max_id']
        return (max_global_id or 0) + 1

    def save(self, *args, **kwargs):
        if self.global_id is None:
            self.global_id = self.get_next_global_id()
        super().save(*args, **kwargs)
# models.py
from django.db import models

class DiseaseDescription(models.Model):
    disease_name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.disease_name
from django.db import models
from django.contrib.auth.models import User

class MedicalHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    height = models.FloatField(default=170.0)  # You might want to use specific units, e.g., centimeters
    weight = models.FloatField(default=70.0) 
    age = models.IntegerField()
    history = models.TextField()  # For medical history details
    blood_group = models.CharField(max_length=3, choices=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ],
    default='O+'
    )
    def __str__(self):
        return f"{self.name}'s Medical History"