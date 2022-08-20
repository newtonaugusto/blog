
from django.db import models

from business.choices.status import Status
from business.choices.type_article import TypeArticle


class Article(models.Model):

    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    type_article = models.IntegerField(choices=TypeArticle.choices)
    content = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices)


class Keyword(models.Model):

    name = models.CharField(max_length=50)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE,
        related_name="keyword_set", null=True, blank=True)
