"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from DjangoBlog.sitemap import StaticViewSitemap, ArticleSiteMap, CategorySiteMap, TagSiteMap, UserSiteMap
from DjangoBlog.feeds import DjangoBlogFeed
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {

    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
    'User': UserSiteMap,
    'static': StaticViewSitemap
}

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'

urlpatterns = [
                  re_path(r'^admin/', admin.site.urls),
                  re_path(r'', include('blog.urls')),

                  re_path(r'', include('comments.urls')),
                  re_path(r'', include('accounts.urls')),
                  re_path(r'', include('oauth.urls')),
                  re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                          name='django.contrib.sitemaps.views.sitemap'),
                  re_path(r'^feed/$', DjangoBlogFeed()),
                  re_path(r'^search', include('haystack.urls')),
                  re_path(r'', include('servermanager.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
