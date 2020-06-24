from django.conf.urls import *
import clients.views

urlpatterns = [
    url(
        regex="^manager_dashboard/clients/?$",
        view=clients.views.manager_client_dashboard,
        name='manager_dashboard_clients'
    ),
]
