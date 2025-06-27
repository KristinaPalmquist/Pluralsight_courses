from django.contrib import admin
from django.urls import path, include
from website.views import welcome, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('', welcome, name='welcome'),
    path('meetings/', include('meetings.urls')),
    path('auth/', include('django.contrib.auth.urls'))
]
