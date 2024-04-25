from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from core.views import IndexView

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('backend.api')),
    re_path(r'^.*$', IndexView.as_view()),  # catch-all route to serve the SPA
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
