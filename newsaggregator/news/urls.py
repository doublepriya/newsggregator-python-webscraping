from django.urls import path
from news.views import scrape, news_list,statichome
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('news/', news_list, name="home"),
  path('', statichome, name="statichome"),
]