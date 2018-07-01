from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('post.urls')),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
]
