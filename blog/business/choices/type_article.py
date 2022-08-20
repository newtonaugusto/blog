
from django.db.models import IntegerChoices


class TypeArticle(IntegerChoices):

    SCIENTIFIC = 0
    PUBLICITY = 1
    INTERVIEW = 2
