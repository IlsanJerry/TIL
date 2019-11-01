from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('students/', include('students.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
