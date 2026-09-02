from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
    
    # Force Static Files Serving (Every environment)
    path("static/<path:path>", serve, {"document_root": settings.STATIC_ROOT}),
    
    # Force Media Files Serving (Fix for Render ephemeral storage)
    path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
]