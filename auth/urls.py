from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.PictureView.as_view()),
    url(r'^upload_picture', views.upload_picture, name='upload_picture'),
]