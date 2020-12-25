"""foodgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path
from django.views.generic import RedirectView

handler404 = "snot.views.page_not_found" # noqa
handler500 = "snot.views.server_error" # noqa


urlpatterns = [
    # регистрация и авторизация
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),

    path('', include('snot.urls')),
    path('', include('recipe.urls')),
    path('', include('users.urls')),

    # раздел администратора
    path("admin/", admin.site.urls),

    # flatpages
    path("about/", include("django.contrib.flatpages.urls")),
    path('author/', views.flatpage, {'url': '/author/'}, name='author'),
    path('spec/', views.flatpage, {'url': '/spec/'}, name='spec'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.png'), name='favicon'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
