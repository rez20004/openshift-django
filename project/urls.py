from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from welcome.views import health
schema_view = get_swagger_view(title='Edu API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/', include('universities.urls')),
    url(r'^health/$', health, name='health'),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
