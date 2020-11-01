from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.message,name="mesg"),
    path('appointment',views.appointments,name="appointment"),
    path('success/',views.success,name="success"),
    path('confirm/',views.confirm,name="confirm")
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)