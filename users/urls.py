from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # include default authentication urls
    path('', include('django.contrib.auth.urls'))
]
