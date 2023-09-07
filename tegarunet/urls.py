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
from rents import views as rent_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Job related views
    path('users/', user_views.register, name='register'),
    path('jobs/', job_views.JobtListView.as_view(), name='jobs'),
    path('jobs/new', job_views.JobCreateView.as_view(), name='job-new'),
    path('jobs/<int:pk>/', job_views.JobDetailView.as_view(), name='job-detail'),
    path('jobs/<int:pk>/update', job_views.JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete', job_views.JobDeleteView.as_view(), name='job-delete'),
    path('jobs/<int:pk>/apply', job_views.JobApplicationView.as_view(), name='job-apply'),
    # urls for rents
    path('rents/', rent_views.Item4RentListView.as_view(), name='rents'),
    path('rents/new', rent_views.RentCreateView.as_view(), name='rent-create'),
    path('rents/<int:pk>/', rent_views.RentDetailView.as_view(), name='item-detail'),
    path('rents/<str:username>/', rent_views.UserRentsListView.as_view(), name='user-rents'),
    path('rents/<int:pk>/update', rent_views.RentUpdateView.as_view(), name='rent-update'),
    path('rents/<int:pk>/delete', rent_views.RentDeleteView.as_view(), name='rent-delete'),
    #path('rents/<int:pk>/apply', rent_views.RentApplicationView.as_view(), name='rent-apply'),
    # user related urls
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password-reset-complete'),
    path('', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)