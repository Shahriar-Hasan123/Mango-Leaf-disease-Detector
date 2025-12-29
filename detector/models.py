from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    treatment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Prediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    disease = models.CharField(max_length=100)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.disease} ({self.confidence:.2f})"