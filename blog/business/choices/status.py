
from django.db.models import IntegerChoices


class Status(IntegerChoices):
    PUBLIC = 0
    PRIVATE = 1
