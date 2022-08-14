from django.urls import path
from .views import ArticleList , ArtileDetail


urlpatterns = [
    path('', ArticleList.as_view() , name = 'Arlist'),
    path('<int>pk>', ArtileDetail.as_view() , name = 'Ardetail'),
]