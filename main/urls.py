from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news_list, name='news'),
    url(r'^(?P<new_id>\d+)/$', views.new_detail, name='new_detail'),
]
