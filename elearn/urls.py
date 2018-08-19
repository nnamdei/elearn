"""elearn path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path(r'^$', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.conf.paths import path, include
    2. Add a path to pathpatterns:  path(r'^blog/', include('blog.paths'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('courselist/',CourseListView.as_view(),name='course_list'),
     path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('students/',include('students.urls')),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


