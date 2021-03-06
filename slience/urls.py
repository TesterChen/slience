"""slience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include,url
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token,refresh_jwt_token

from rest_framework import routers
from accounts import views as accounts_views
from taskManager import views as taskManager_views
from reportManager import views as reportManager_views

router = routers.DefaultRouter()
router.register(r'users',accounts_views.UserViewSet)
router.register(r'tasks',taskManager_views.PeriodicViewSet)
router.register(r'schedules',taskManager_views.CrontabScheduleViewSet)
router.register(r'reports',reportManager_views.ReportViewSet)


urlpatterns = [
    url(r'^api/',include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/report-upload/(?P<filename>[^/]+)$', reportManager_views.ReportFileView.as_view()),
    url(r'^api/suite-run/$', taskManager_views.RunTestView.as_view()),

]
