# Generated by Django 4.2.6 on 2023-10-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endangeredanimal',
            name='CommonName',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='endangeredanimal',
            name='FishingVulnerability',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='endangeredanimal',
            name='IUCNRedListStatus',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='endangeredanimal',
            name='Resilience',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='endangeredanimal',
            name='Salinity',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='endangeredanimal',
            name='ThreatsToHumans',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]