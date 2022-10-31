from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=21)
    frequency = models.IntegerField(default=0)
    ngram_score = models.FloatField(default=0.0)