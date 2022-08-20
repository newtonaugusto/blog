
from rest_framework import serializers
from business.models import Article, Keyword

from business.choices.status import Status
from business.choices.type_article import TypeArticle


class KeywordSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class ArticleSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    title = serializers.CharField(min_length=2, max_length=50)
    subtitle = serializers.CharField(max_length=150)
    type = serializers.ChoiceField(
        choices=TypeArticle.choices, required=False, source="type_article")
    content = serializers.CharField()
    status = serializers.ChoiceField(choices=Status.choices)
    keyword_set = KeywordSerializer(required=False, many=True)

    class Meta:
        model = Article
        ref_name = "Artigo"
        fields = (
            "id", "title", "subtitle", "type",
            "content", "status", "keyword_set")

    def create(self, validated_data):
        keyword_set = validated_data.pop("keyword_set", None)
        article = Article.objects.create(**validated_data)
        if keyword_set:
            keywords = [
                Keyword.objects.create(**keyword) for keyword in keyword_set]
            article.keyword_set.set(keywords)
        return article

    def update(self, instance, validated_data):
        keyword_set = validated_data.pop("keyword_set", None)
        if keyword_set:
            keywords = Keyword.objects.bulk_create(keyword_set)

        instance.keyword_set.remove(instance.keyword_set)
        for item in validated_data:
            if Article._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        instance.save()

        instance.keyword_set.set(keywords)
        return instance


class ArticleDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    subtitle = serializers.CharField()
    type = serializers.IntegerField(source="type_article")
    content = serializers.CharField()
    status = serializers.IntegerField()
    keyword_set = KeywordSerializer(many=True)


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    subtitle = serializers.CharField()
    type = serializers.IntegerField(source="type_article")
    content = serializers.CharField()
    status = serializers.IntegerField()
    keyword_set = KeywordSerializer(many=True)
