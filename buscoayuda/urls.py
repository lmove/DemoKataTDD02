from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'buscoayuda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('componentes.urls',namespace='independiente')),
    url(r'^admin/', include(admin.site.urls)),
]
