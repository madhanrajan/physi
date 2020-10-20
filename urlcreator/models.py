from django.db import models

# Create your models here.


class PDFRetriever(models.Model):
    token = models.TextField(unique=True)
    pdf_url = models.TextField()
