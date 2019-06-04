"""cbvs_mongo_upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.urls import include, url
from cbvs_mongo_app import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.Registration),
    path('esend/',views.Email_Send_View),
    
    path('$/',views.CurdListView.as_view(),name='Emp'),
    url(r'^(?P<pk>\d+)/$',views.CurdDetailView.as_view(),name='detail'),
    path('create/',views.CurdCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$',views.CurdUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$',views.CurdDeleteView.as_view()),

    path('cookie/',views.cookies_count_view),
    path('session/',views.page_count_view),
    path('formset/',views.FormSet_BookListView),
    path('fakedata/',views.fake_data),
    path('fakephone/',views.fake_phone)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)