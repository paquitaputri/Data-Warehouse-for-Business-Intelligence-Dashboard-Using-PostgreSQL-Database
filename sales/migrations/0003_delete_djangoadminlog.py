# Generated by Django 3.1.2 on 2020-11-04 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
    ]
