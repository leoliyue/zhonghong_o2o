from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpRequest
from django.http import HttpResponseRedirect
from django.template import loader
from Fangfull.model.m_Album import Album
from Fangfull.model.m_Content_sql import Content_sql
from Fangfull.model.m_Content_url import Content_url
from Fangfull.model.m_Res_requests import Res_requests
from Fangfull.model.m_Res_data import Res_data
import json
from Fangfull.model.m_Song import Song
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView



# class IndexView(generic.ListView):
#     template_name = 'fangfull/index.html'
#     context_object_name = 'all_albums'
#     def get_queryset(self):
#         return Album.objects.all()
#
# class DetailView(generic.DeleteView):
#     model = Album
#     template_name = 'fangfull/detail.html'
#
# class ContentUrlView(generic.ListView):
#     template_name = 'fangfull/viewContenturl.html'
#     context_object_name = 'all_contenturl'
#     def get_queryset(self):
#         return Content_url.objects.all()
#
#
# class ContentSqlView(generic.ListView):
#     model = Content_url
#     print(model)
#     template_name = 'fangfull/viewContentsql.html'
    # context_object_name = 'get_contentsql'
    # getattr()
    # def get_queryset(self):
    #     return Content_sql.objects.get(sql_id = 1)




# class ContentSqlView(generic.ListView):
#     # print('333')
#     model = Content_url.sql
#     template_name = 'fangfull/viewContentsql.html'
    #
    # template_name = 'fangfull/viewContentsql.html'
    # context_object_name = 'get_contentsql'
    # def get_queryset(self):
    #     return Content_sql.objects.get(sql_name ='2')
#
#
#
# class ContentSqlCreate(CreateView):
#     model = Content_sql
#     fields = ['sql_name','sql_host','sql_port','sql_user_name','sql_user_passwd','sql_db','sql_type']


#----------------------------
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'fangfull/index.html',{'all_albums':all_albums})

def detail(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'fangfull/detail.html',{'album':album})

def Setting(request):
    all_contenturl = Content_url.objects.all()
    all_contentsql = Content_sql.objects.all()
    return render(request,'fangfull/setting.html',{'all_contenturl': all_contenturl, 'all_contentsql': all_contentsql} )

def ViewContentUrl(request):
    all_contenturl = Content_url.objects.all()
    return render(request, 'fangfull/viewContenturl.html',{'all_contenturl':all_contenturl})

def NewContentUrl(request):
    centent = Content_sql.objects.values_list('sql_id','sql_name')
    typemessage = []
    Sqlmessage = []
    for i in range (len(centent)):
        for j in range (len(centent[i])):
            typemessage.append(centent[i][j])
        Sqlmessage.append(typemessage)
        typemessage = []
    Sqlmessage = []
    for i in range (len(centent)):
        sql_id = centent[i][0]
        sql_name = centent[i][1]
        Sqlmessage.append({'sql_id':sql_id,'sql_name':sql_name})
    return render(request,'fangfull/creatContenturl.html',{'Sqlmessage':Sqlmessage})

def SaveContentUrl(request):
    url_blue = request.POST['url_blue']
    url_red = request.POST['url_red']
    url_type = request.POST['url_type']
    url_stuts = request.POST['url_stuts']
    sql_id = request.POST['sql_id']
    content_url = Content_url()
    content_url.url_blue = url_blue
    content_url.url_red = url_red
    content_url.url_type = url_type
    content_url.url_stuts = url_stuts
    content_url.sql_id = sql_id
    content_url.save()
    return HttpResponseRedirect('/Fangfull/contenturl/new/')

def ContentUrlSql(request,sql_id):
    get_contenturl =  Content_sql.objects.get(sql_id=sql_id)
    return render(request,'fangfull/viewContentsql.html',{'get_contenturl':get_contenturl})


def ViewRequests(requset,url_id):
    all_requests = Res_requests.objects.all()
    # requests_id = []
    # for i in all_requests:
    #     requests_id.append(i.requests_id)
    return render(requset,'fangfull/request/viewRequest.html',{'all_requests':all_requests,'url_id':url_id})


def NewRequests(request):


    return render(request,'fangfull/request/creatRequests.html')

def SaveRequests(request):

    return render(request,'fangfull/request/viewRequest.html')

def ViewRequests_data(request):
    all_ResData = Res_data.objects.all()
    return render(request,'fangfull/request/viewRequest_data.html',{'all_ResData':all_ResData})

def GetRequests_data(request,url_id,requests_id):
    get_requests = Res_requests.objects.get(requests_id=str(requests_id))
    list_requests_data = list(get_requests.requests_data)
    for li in list_requests_data:
        if li == ',':
            list_requests_data.remove(li)
    data = []
    for i in range (len(list_requests_data)):
        data.append(Res_data.objects.get(data_id = list_requests_data[i]))
    return render(request,'fangfull/request/getRequest_data.html',{'all_data':data})


