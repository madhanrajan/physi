from django.db import models

# Create your models here.


class FeedbackData(models.Model):
    data = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data
