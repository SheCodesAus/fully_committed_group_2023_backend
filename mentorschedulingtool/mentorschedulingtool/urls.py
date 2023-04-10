"""mentorschedulingtool URL Configuration

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
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

# API Root ---
from mentors.views import api_root

urlpatterns = [
    path("", api_root),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('mentors.urls')),
    path('', include('sess.urls')),
    path('', include('programs.urls')),
    path("api-auth/", include("rest_framework.urls")),  # adds login button
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),  # adds generate token url
    path('', include("users.urls")),
]

admin.site.site_header = "Return To: Mentor Scheduling Tool"