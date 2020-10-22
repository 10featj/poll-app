from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers 
from poll import views

router = routers.DefaultRouter()
router.register(r'polls', views.PollView, 'poll')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]