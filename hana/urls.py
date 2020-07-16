"""hana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from hana import views
from hana.views import login
from social import views as sview
from social.views import PlatformsListView, PlatformsDetailView, SocialListView
from photos import urls
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.static import serve
from hana.views import SignUp
from hana import views, settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='redirect'),
    #path('home/', views.home, name='home'),
    path('home/', sview.PlatformsListView.as_view(), name='home'),
    path('social/', sview.SocialListView.as_view(), name='main-social'),
    path('social/<int:pk>/', sview.PlatformsDetailView.as_view(), name='platform_detail'),
    path('journals/', include('myjournal.urls')),
    path('photos/', include('photos.urls')),
    path('videos/', include('videos.urls')),
    path('documents/', include('documents.urls')),
    path('schedule/', include('schedule.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='hana/login.html'), name='login'),
    path('register/', views.SignUp.as_view(), name='register'),
    #path('accounts/', include('django.contrib.auth.urls')),
   # path('login/', views.login, name='login'),
    #path('accounts/', include('social.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
'''
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
'''
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
