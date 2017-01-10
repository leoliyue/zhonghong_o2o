from django.contrib import admin
# from .models import Album,Song
from Fangfull.model import m_Album,m_Song,m_Message_res,m_Message_data

from Fangfull.model import m_Res_requests,m_Res_data,m_Res_data_value
admin.site.register(m_Album.Album)
admin.site.register(m_Song.Song)
admin.site.register(m_Message_res.Message_res)
admin.site.register(m_Message_data.Message_data)
admin.site.register(m_Res_requests.Res_requests)
admin.site.register(m_Res_data.Res_data)
admin.site.register(m_Res_data_value.Res_data_value)
