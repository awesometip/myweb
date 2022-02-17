from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dust_checker', include('dust_checker.urls')),
    path('bike', include('bike.urls')),
    path('gcash', include('gcash.urls')),
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
