from __future__ import unicode_literals

# Without using spatial db
from django.db import models as pmodels
from location_field.models.plain import PlainLocationField

# Django location field using spatial db
from django.contrib.gis.db import models as smodels
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField


# Create your models here.

class SpatialPlace(smodels.Model):
    city = smodels.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    objects = smodels.GeoManager()

class Place(pmodels.Model):
    city = pmodels.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)