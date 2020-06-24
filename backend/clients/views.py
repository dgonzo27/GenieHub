from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse, Http404, HttpResponse
from .models import Client

from logging import getLogger

logger = getLogger("clients.views")

# base view for this application
@permission_required('clients.view_client_dashboard', raise_exception=True)
def manager_client_dashboard(request):
    logger.debug('client_dashboard')
    
    # Only allow super users to access this page
    if not request.user.is_superuser:
        return HttpResponse(status=404)

    # TODO
    clients = Client.objects.filter(inactive=False)

    return JsonResponse({"clients": clients})


def char_count(request):
    text = request.GET.get("text", "")

    return JsonResponse({"count": len(text)})