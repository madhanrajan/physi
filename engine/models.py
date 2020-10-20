from django.db import models
import os
from django.conf import settings
from tika import parser
# Create your models here.


class Subject(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to="book/%Y/%m/%d",blank=True)
    subject = models.ManyToManyField(
        Subject, related_name='subjects')

    def delete(self, using=None, keep_parents=False):
        self.document.storage.delete(self.document.name)
        super().delete(using=using,keep_parents=keep_parents)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.TextField(max_length=200, blank="False")
    source_file = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='topic')
    create_date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to="topic/%Y/%m/%d")

    def add_tags(self, tag_list):
        tags = tag_list.split(",")

        for t in tags.lower():
            (_, _) = self.tags.get_or_create(text=t)

    def get_document_text(self):

        raw = parser.from_file(self.document.url)
        return raw['content']

    def get_book_title(self):
        return self.source_file.title

    def get_book_description(self):
        return self.source_file.description

    def get_subject_list(self):
        return [subject.title for subject in self.source_file.subject.all()]

    def delete(self, using=None, keep_parents=False):
        self.document.storage.delete(self.document.name)
        super().delete(using=using,keep_parents=keep_parents)

    def __str__(self):
        return self.title


class Tag(models.Model):
    text = models.TextField(max_length=50, unique=True)
    approved = models.BooleanField(default=False)
    tags = models.ManyToManyField(Topic, related_name="tags")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
