from django.urls import path
from .views import UserList
app_name='api'


urlpatterns = [
    path('list', UserList.as_view(),name='userlist_api'),
   

]
