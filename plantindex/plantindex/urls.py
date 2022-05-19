from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from plants import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('plants/<int:plant_id>/', views.plant_detail, name='plant_detail')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



