from django.db import models
from pgvector.django import VectorField

class Document(models.Model):
    content = models.TextField()
    embedding = VectorField(dimensions=1536) # <-- สำคัญมาก: dimensions ต้องตรงกับโมเดลที่ใช้