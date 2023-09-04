"""
URL configuration for tegarunet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from jobportal import views as job_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_views.register, name='register'),
    path('jobs/', job_views.JobtListView.as_view(), name='jobs'),
    path('jobs/new', job_views.JobCreateView.as_view(), name='job-new'),
    path('jobs/<int:pk>/', job_views.JobDetailView.as_view(), name='job-detail'),
    path('jobs/<int:pk>/update', job_views.JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete', job_views.JobDeleteView.as_view(), name='job-delete'),
    path('jobs/<int:pk>/apply', job_views.JobApplicationView.as_view(), name='job-apply'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)