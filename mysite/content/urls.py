from django.urls import path

from content.views import Dashboard, UserProfile, Table, Notifications

app_name = 'content'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('user/', UserProfile.as_view(), name='userprofile'),
    path('table/', Table.as_view(), name='table'),
    path('notifications/', Notifications.as_view(), name='notifications'),
]