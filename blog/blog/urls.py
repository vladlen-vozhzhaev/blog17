"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from hello import views

urlpatterns = [
    path('signup', views.singup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reg', views.handlerReg),
    #path('login', views.handlerLogin),
    path('profile', views.showProfile, name="profile"),
    path('addArticle', views.addArticle),
    path('editArticle/<int:id>', views.editArticle),
    path('article/<int:id>', views.singleArticle),
    path('addComment', views.addComment)
]