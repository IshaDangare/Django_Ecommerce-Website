from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('product',views.product,name='product'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

