from django.conf.urls import url

from chatbot import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^input.html$',views.input,name='input'),
]