"""Define URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # detailed page about certain topic
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
]
