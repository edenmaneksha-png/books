from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

# Wrap frontend view so Django always sets the csrftoken cookie
frontend = ensure_csrf_cookie(TemplateView.as_view(template_name='index.html'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),
    path('', frontend, name='frontend'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
