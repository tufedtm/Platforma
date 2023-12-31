"""
URL configuration for platforma project.

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
from django.urls import path
from assets.utils import update_table
from assets.views import index, terms, contact, LoginUser, logout_user, get_results, pageNotFound
from django.contrib import admin

urlpatterns = [
    # path('api/v1/datafeed/', PlatformaRatesView.as_view(), name='datafeed'),
    path('',index, name='index'),
    path('terms/',terms, name='terms'),
    path('contact/',contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('update_table/', update_table, name='update_table'),
    path('results/', get_results, name='results'),
]
handler404 = pageNotFound
