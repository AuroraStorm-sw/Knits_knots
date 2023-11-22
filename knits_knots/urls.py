from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('company/', include('company.urls',)),
    path('products/', include('products.urls',)),
    path('basket/', include('basket.urls',)),
    path('checkout/', include('checkout.urls',)),
    path('wishlist/', include('wishlist.urls',)),
    path('profile/', include('profile.urls',)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'knits_knots.views.handler404'
