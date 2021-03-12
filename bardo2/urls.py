from django.contrib import admin
from django.urls import path, include

from web.views import IndexView
from websocket.urls import websocket
from websocket.views import websocket_view


urlpatterns = [
    path('world/', include('world.urls')),
    path('admin/', admin.site.urls),
    websocket("ws/", websocket_view),
    path('', include('web.urls')),
]
