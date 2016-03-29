from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<value>\d+)/$', views.index_por_servicio, name='index_por_servicio'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^perfil/(?P<value>\d+)/$', views.actualizar_independiente, name='actualizar_independiente'),
    url(r'^get_service/', views.get_service, name='get_service'),
    url(r'^post_register/', views.post_register, name='post_register'),
    url(r'^post_login/', views.post_login, name='post_register'),
    url(r'^servicio/', views.ver_servicios, name='ver_servicios'),
    url(r'^comentario/', views.crear_comentario, name='crear_comentario'),
    url(r'^detalle/(?P<value>\d+)/$', views.detalle_independiente, name='detalleIndependiente'),
    url(r'^independiente/(?P<value>\d+)/comentario/', views.ver_comentarios, name='verComentarios'),

    url(r'^api/login/', views.api_login, name='api_login'),
    url(r'^api/independientes/servicios/(?P<value>\d+)/$', views.api_independientes_por_servicio, name='api_independientes_por_servicio'),
    url(r'^api/independientes/(?P<value>\d+)/comentarios/', views.api_comentarios_por_independiente, name='api_comentarios_por_independiente'),
    url(r'^api/independientes/(?P<value>\d+)/', views.api_independientes_por_id, name='api_independientes_por_id'),
    url(r'^api/independientes/', views.api_independientes, name='api_independientes'),
    url(r'^api/servicios/', views.api_servicios, name='api_servicios'),
    url(r'^api/comentarios/', views.api_comentarios, name='api_comentarios'),
]
