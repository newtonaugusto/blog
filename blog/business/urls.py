
from django.urls import path

from business import views


app_name = 'business'


urlpatterns = [
    path('articles', views.ArticleView.as_view({
        "post": "create",
        "get": "list"
    }), name='articles'),

    path('articles/<int:id>', views.ArticleView.as_view({
        "get": "get",
        "put": "update",
        "delete": "delete"
    }), name='articles'),
]
