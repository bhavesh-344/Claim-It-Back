from django.contrib import admin
from django.urls import path ,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name="home"),
    path('reportFound/',include("found.urls")),
    path('claimNow/<int:id>/',views.claimNow , name="claimNow")
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
