from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

import views

router = DefaultRouter()

router.register(r'', views.UserViewSet, base_name='users')

# urlspatterns = [
#
# ]

urlpatterns = router.urls