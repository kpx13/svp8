#encoding=utf8

from django.conf.urls.defaults import url, patterns

from . import views
from .utils.decorators import room_check_access
from .ajax import chat

urlpatterns = patterns('chatrooms',
    # ajax requests
    url(r'^get_messages/', chat.ChatView().get_messages),
    url(r'^send_message/', chat.ChatView().send_message),
    url(r'^get_latest_msg_id/', chat.ChatView().get_latest_message_id),
    url(r'^get_users_list/$', chat.ChatView().get_users_list),
    url(r'^notify_users_list/$', chat.ChatView().notify_users_list),
)
