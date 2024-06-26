# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DimKategori(models.Model):
    kategori_id = models.AutoField(primary_key=True)
    nama_kategori = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'dim_kategori'


class DimKota(models.Model):
    kota_id = models.AutoField(primary_key=True)
    provinsi = models.ForeignKey('DimProvinsi', models.DO_NOTHING, blank=True, null=True)
    kota_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_kota'


class DimModePengiriman(models.Model):
    mode_pengiriman_id = models.IntegerField(primary_key=True)
    nama_mode_pengiriman = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_mode_pengiriman'


class DimNegara(models.Model):
    negara_id = models.AutoField(primary_key=True)
    region = models.ForeignKey('DimRegion', models.DO_NOTHING, blank=True, null=True)
    nama_negara = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_negara'


class DimPelanggan(models.Model):
    pelanggan_id = models.TextField(primary_key=True)
    nama_pelanggan = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_pelanggan'


class DimPesanan(models.Model):
    pesanan_id = models.TextField(primary_key=True)
    produk = models.ForeignKey('DimProduk', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_pesanan'

    def __str__(self):
        return str(self.pesanan_id)


class DimProduk(models.Model):
    produk_id = models.TextField(primary_key=True)
    subkategori = models.ForeignKey('DimSubkategori', models.DO_NOTHING, blank=True, null=True)
    nama_produk = models.TextField()
    tipe_produk = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_produk'


class DimProvinsi(models.Model):
    provinsi_id = models.IntegerField(primary_key=True)
    negara = models.ForeignKey(DimNegara, models.DO_NOTHING, blank=True, null=True)
    nama_provinsi = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_provinsi'


class DimRegion(models.Model):
    region_id = models.AutoField(primary_key=True)
    nama_region = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'dim_region'


class DimSegmen(models.Model):
    segmen_id = models.IntegerField(primary_key=True)
    nama_segmen = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_segmen'


class DimSubkategori(models.Model):
    subkategori_id = models.AutoField(primary_key=True)
    kategori = models.ForeignKey(DimKategori, models.DO_NOTHING, blank=True, null=True)
    nama_subkategori = models.TextField()

    class Meta:
        managed = False
        db_table = 'dim_subkategori'


class DimWaktu(models.Model):
    tanggal_id = models.AutoField(primary_key=True)
    hari = models.TextField()
    tanggal = models.DateField()

    class Meta:
        managed = False
        db_table = 'dim_waktu'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FaktaPengiriman(models.Model):
    nomer = models.AutoField(primary_key=True)
    pesanan = models.ForeignKey(DimPesanan, models.DO_NOTHING, blank=True, null=True)
    mode_pengiriman = models.ForeignKey(DimModePengiriman, models.DO_NOTHING, blank=True, null=True)
    kota = models.ForeignKey(DimKota, models.DO_NOTHING, blank=True, null=True)
    pelanggan = models.ForeignKey(DimPelanggan, models.DO_NOTHING, blank=True, null=True)
    tanggal = models.ForeignKey(DimWaktu, models.DO_NOTHING, blank=True, null=True)
    barang_diterima = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fakta_pengiriman'

    def __str__(self):
        return str(self.nomer, self.pesanan, self.mode_pengiriman, self.kota, self.pelanggan, self.tanggal, self.barang_diterima)


class FaktaPenjualan(models.Model):
    nomer = models.AutoField(primary_key=True)
    pesanan = models.ForeignKey(DimPesanan, models.DO_NOTHING, blank=True, null=True)
    kota = models.ForeignKey(DimKota, models.DO_NOTHING, blank=True, null=True)
    tanggal = models.ForeignKey(DimWaktu, models.DO_NOTHING, blank=True, null=True)
    pelanggan = models.ForeignKey(DimPelanggan, models.DO_NOTHING, blank=True, null=True)
    segmen = models.ForeignKey(DimSegmen, models.DO_NOTHING, blank=True, null=True)
    harga = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    profit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jumlah_barang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fakta_penjualan'

    def __unicode__(self):
        return '%s' % self.nomer

    def __str__(self):
        return str(self.nomer, self.pesanan, self.kota, self.tanggal, self.pelanggan, self.segmen, self.harga, self.profit, self.jumlah_barang)
