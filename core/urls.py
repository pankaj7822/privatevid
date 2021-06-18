from django.urls import path
from .views import home,getlocation,botrequest,fakefb,fetchvideo
urlpatterns = [
    path('',home),
    path('loc/',getlocation),
    path('bot/',botrequest),
    path('fetchvideo/',fetchvideo)
    # path('flogin/',fakefb)
]