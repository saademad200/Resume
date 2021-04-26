from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    # url(r'^$', ,),
    url(r'', views.resumeFill, name='resume_fill'),
    url(r'^resumeview', views.resumeView, name='resume_view'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
