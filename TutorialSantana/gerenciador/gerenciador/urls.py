from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    (r'^$', "agenda.views.lista"),
    (r'^adiciona/$', "agenda.views.adiciona"),
    (r'^item/(?P<nr_item>\d+)/$', "agenda.views.item"),
    (r'^remove/(?P<nr_item>\d+)/$', "agenda.views.remove"),

    (r'^login/', "django.contrib.auth.views.login", {
    	"template_name": "login.html"}),
    (r'^logout/', "django.contrib.auth.views.logout_then_login", {
    	'login_url': '/login/'}),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)