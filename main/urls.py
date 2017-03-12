from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^$', views.news_list, name='index'),
    url(r'^(?P<new_id>\d+)/$', views.new_detail, name='new_detail'),
]