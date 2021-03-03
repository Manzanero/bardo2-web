from django.contrib import admin
from django.urls import path
from websocket.urls import websocket
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view()),
    websocket("ws/", views.websocket_view),
]
