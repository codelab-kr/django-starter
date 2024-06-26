"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("", views.homepage),
    path("home", views.homepage, name="home"),
    path("boss", admin.site.urls, name="admin"),
    path("about/", views.about, name="about"),
    path("posts/", include("posts.urls")),
    path("users/", include("users.urls")),
    path("acts/", include("acts.urls")),
    path("tasks/", include("tasks.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
