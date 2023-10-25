from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.conf import settings

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('programs/', include('edu_progs.urls', namespace='edu_progs')),
    path('news/', include('news.urls', namespace='news')),
    path('events/', include('events.urls', namespace='events')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
