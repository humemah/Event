from django.urls import path
from . import views
urlpatterns=[
    path("",views.home, name="home"),
    path("login_user", views.login_user, name="login"),
    path("register_user", views.register_user, name="Registration"),
    path('add_event', views.add_event, name='Event'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('display_event', views.display_event, name='display_event'),
    path('event_update/<event_id>', views.event_update, name='event_update'),
    ]
