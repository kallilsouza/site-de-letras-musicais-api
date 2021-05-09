from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView

urlpatterns = (
    [
        # # path("admin/", admin.site.urls),
        re_path(r"^admin/.*$", RedirectView.as_view(url="/pt-br/admin/"), name="index"),
        re_path(
            r"^en/admin/.*$", RedirectView.as_view(url="/pt-br/admin/"), name="index"
        ),
        re_path("", include("api.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + i18n_patterns(
        path("admin/", admin.site.urls),
    )
)
