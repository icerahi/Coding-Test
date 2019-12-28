from django.urls import path
from . import views
urlpatterns = [

    path('GET/values/',views.list,name='list'),
    path('POST/values/',views.post,name='post'),
    path('PATCH/values/',views.update,name='update'),
    path('GET/values/keys=<keys>/',views.with_keys, name='withkeys'),

]
