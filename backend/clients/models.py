from django.db import models
from django.core.exceptions import ValidationError
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.urls import reverse
from logging import getLogger
from rest_framework import serializers

logger = getLogger('client.models')

# You can copy and paste this in each of your sub app models.py file
# No database table creation or deletion operation will be performed for this model
# These are permissions you can set up and use across your application

# Okay guess not fuck that
# class AppPermissions(models.Model):
#     class Meta:
#         managed = False

#         permissions = ( 
#             ('view_client_dashboard_own', 'Can view own client dashboard'),
#             ('view_client_dashboard', 'Can view any given client dashboard (admin)'),
#             ('view_team_profile_own', 'Can view own client team/resources profiles'),
#             ('view_team_profile', 'Can view any given client team/resoures profiles (admin)'),
#         )


def client_logo_path(instance, filename):
    return 'client_logos/client_{0}/{1}'.format(instance.pk, filename)

class Client(models.Model):
    """
    A client is a TechGenies customer, typically someone with a development team and a product
    """
    name = models.CharField(max_length=100, help_text='The name of this client')
    # logo = models.FileField(blank=True, null=True, upload_to=client_logo_path, validators=[FileExtensionValidator(extensions=['jpg', 'png'])])
    notifications_enabled = models.BooleanField(default=True, help_text='Deliver email/sms notifications to users associated with this client')
    inactive = models.BooleanField(default=False, help_text='Mark old clients inactive to keep data w/out deleting')

    # TODO 
    # team_profiles = models.ManyToManyField(TeamProfile, blank=True, help_text='The developers or resources for this client')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @staticmethod
    def get_serializer():
        return import_string('clients.serializers.ClientSerializer')