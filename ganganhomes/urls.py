from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 
from django.contrib.auth import views
from django.urls import path, include


from core.views import frontPage, shop, signup

urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
