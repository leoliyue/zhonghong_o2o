from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^album/$',views.index,name='index'),
    #/Fangfull/721/
    url(r'^song/(?P<album_id>[0-9]+)$',views.detail,name='detail'),

    url(r'^setting',views.Setting,name='setting'),


    url(r'^contenturl/$', views.ViewContentUrl , name='viewContenturl'),
    url(r'^contentsql/(?P<sql_id>[0-9]+)$', views.ContentUrlSql , name='viewContentsql'),
    url(r'^contenturl/new/$', views.NewContentUrl, name = 'newContentUrl'),
    url(r'^contenturl/new/save/$', views.SaveContentUrl, name = 'saveContentUrl'),


    url(r'^request/(?P<url_id>[0-9]+)/$',views.ViewRequests, name='viewRequest'),
    url(r'^request/new/$',views.NewRequests, name='newRequests'),
    url(r'^request/new/save/$',views.SaveRequests, name='saveRequests'),

    url(r'^requestdata/$',views.ViewRequests_data,name='viewRequestData'),
    url(r'^requestdata/(?P<url_id>[0-9]+)/getviewdata/(?P<requests_id>[0-9]+)/$',views.GetRequests_data,name='getRequestData'),




]
