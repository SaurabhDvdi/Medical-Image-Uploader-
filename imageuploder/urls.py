
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from imageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('sign_in/',views.sign_in, name='sign_in'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
