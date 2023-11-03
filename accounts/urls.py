from . import views
from django.urls import path

app_name='accounts'

urlpatterns = [
    path('',views.home , name='home'),
    path('register/',views.registration , name='register'),
    path('logout/',views.logout_view , name='logout'),
]
