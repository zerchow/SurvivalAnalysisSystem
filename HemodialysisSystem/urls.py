"""HemodialysisSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
import runoob_view
import runoob_testdb
import runoob_search
import os
import sa_test
import home_view

dirname = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')

urlpatterns = [
    url(r'^hello/', runoob_view.hello),
    url(r'^testdb/', runoob_testdb.testdb),
    url(r'^search/', runoob_search.search),
    url(r'^search_process_get/', runoob_search.search_process_get),
    url(r'^search_process_post/', runoob_search.search_process_post),
    url(r'^images/(?P<path>.*)', 'django.views.static.serve', {'document_root': dirname + '/images'}),
    url(r'^lena$', runoob_view.get_image),
    url(r'^satest/', sa_test.get_sa),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view.main_page)
]

