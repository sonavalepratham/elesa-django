from django.contrib import admin
from django.urls import path
from viewboard import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path('HandleLogin',views.HandleLogin,name='login'),
    path('HandleLogout',views.HandleLogout,name='logout'),
    path('viewboard',views.viewboard,name='viewboard'),
    path('Register',views.Register,name='Register'),
    path('UpdateProfile',views.UpdateProfile,name='UpdateProfile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)