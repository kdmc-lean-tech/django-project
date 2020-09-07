from django.urls import path
from .views import articleList, createArticle, getDeleteAndUpdateArticleById

urlpatterns = [
    path('articles', articleList),
    path('article', createArticle),
    path('article/<pk>', getDeleteAndUpdateArticleById)
]
