# Generated by Django 3.1.2 on 2020-11-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0003_delete_djangoadminlog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DimCategory',
        ),
        migrations.DeleteModel(
            name='DimCity',
        ),
        migrations.DeleteModel(
            name='DimCountry',
        ),
        migrations.DeleteModel(
            name='DimCustomer',
        ),
        migrations.DeleteModel(
            name='DimOrder',
        ),
        migrations.DeleteModel(
            name='DimOrderdate',
        ),
        migrations.DeleteModel(
            name='DimProduct',
        ),
        migrations.DeleteModel(
            name='DimRegion',
        ),
        migrations.DeleteModel(
            name='DimSegment',
        ),
        migrations.DeleteModel(
            name='DimShipment',
        ),
        migrations.DeleteModel(
            name='DimShippingdate',
        ),
        migrations.DeleteModel(
            name='DimState',
        ),
        migrations.DeleteModel(
            name='DimSubcategory',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='FactLogistic',
        ),
        migrations.DeleteModel(
            name='FactSales',
        ),
    ]