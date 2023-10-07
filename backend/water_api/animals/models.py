from django.db import models


class Ecosystem(models.Model):
    E_CODE = models.IntegerField(unique=True)
    EcosystemName = models.CharField(max_length=255)
    EcosystemType = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Salinity = models.CharField(max_length=255)
    NorthernLat = models.FloatField(null=True, blank=True)
    NrangeNS = models.CharField(max_length=10, null=True, blank=True)
    SouthernLat = models.FloatField(null=True, blank=True)
    SrangeNS = models.CharField(max_length=10, null=True, blank=True)
    WesternLat = models.FloatField(null=True, blank=True)
    WrangeEW = models.CharField(max_length=10, null=True, blank=True)
    EasternLat = models.FloatField(null=True, blank=True)
    ErangeEW = models.CharField(max_length=10, null=True, blank=True)
    Climate = models.CharField(max_length=255, null=True, blank=True)
    TotalCount = models.IntegerField(null=True, blank=True)
    TotalFamCount = models.IntegerField(null=True, blank=True)
    TotalComplete = models.IntegerField(null=True, blank=True)
    LatDegFill = models.IntegerField(null=True, blank=True)
    LatMinFill = models.IntegerField(null=True, blank=True)
    NorthSouthFill = models.CharField(max_length=1, null=True, blank=True)
    LongDegFill = models.IntegerField(null=True, blank=True)
    LongMinFill = models.IntegerField(null=True, blank=True)
    EastWestFill = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.EcosystemName
