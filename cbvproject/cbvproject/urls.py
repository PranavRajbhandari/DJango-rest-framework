"""cbvproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from cbv.views import CourseListView, CourseDetailView
from rest_framework.routers import DefaultRouter
from cbv.views import CourseViewSet

router = DefaultRouter()
router.register('test', CourseViewSet, basename='test')

# from below url pattern  path ('/')    <==== what we want inside this path we will be writing same thing inside router.register
# ('here',courseViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),


    
]
