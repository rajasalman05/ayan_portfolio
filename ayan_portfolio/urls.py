from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
    
    # Static Files: Har environment (Vercel Production + Local) par serve hongi
    path("static/<path:path>", serve, {"document_root": settings.STATIC_ROOT}),
]

# Media Files routing (Development mode ke liye)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)