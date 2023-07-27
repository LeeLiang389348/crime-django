from django.contrib import admin
from django.urls import path
from crime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_page)
]
