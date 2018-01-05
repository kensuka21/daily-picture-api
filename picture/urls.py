from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

import views

router = DefaultRouter()

router.register(r'', views.PictureViewSet, base_name='pictures')

urlpatterns = [
    url(r'upload_picture', views.upload_picture),
    url(r'daily_picture', views.get_daily_picture)
]

urlpatterns += router.urls