"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from django.conf import settings

from django.views import static
from rest_framework_swagger.views import get_swagger_view

# from django.contrib.sitemaps.views import sitemap


schema_view = get_swagger_view(title="Pastebin API")
urlpatterns = [
    url(
        r"^static/(?P<path>.*)$",
        static.serve,
        {"document_root": settings.STATIC_ROOT},
        name="static",
    ),
    url(r"^docs$", schema_view),
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]


handler404 = "blog.views.generic.errors.page_not_found"
handler404 = "blog.views.generic.errors.page_error"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r"^__debug__/", include(debug_toolbar.urls))]
