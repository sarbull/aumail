from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aumail.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 'emailClient.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inbox/$', 'emailClient.views.index'),
    url(r'^email/emailList/$', 'emailClient.views.emailFromFolder'),
    url(r'^email/(?P<emailId>\d+)/$', 'emailClient.views.details'),
    url(r'^readmail/$', 'emailClient.views.readMail'),
    url(r'^reply/$', 'emailClient.views.replyPage'),
    url(r'^agenda/$', 'emailClient.views.agendaTemplate'),
    url(r'^agendajson/$', 'emailClient.views.agendaJson'),
    url(r'^compose/$', 'emailClient.views.composeEmail'),
    url(r'^login/$', 'emailClient.views.loginView'),
    url(r'^authenticate/$', 'emailClient.views.authenticate_user'),
    url(r'^email/logoff/$', 'emailClient.views.logoffView'),
)
