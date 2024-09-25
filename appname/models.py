from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




    def __str__(self):
        return self.email



class Profile(models.Model):
    photo = models.ImageField(upload_to='photo',null=True,blank=True)
    user = models.OneToOneField(CustomUser, null=True,blank=True, on_delete=models.CASCADE, related_name='profil')





class PasswordResetCode(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(minutes=15))

    def is_valid(self):
        return timezone.now() < self.expires_at



# ------ ilaç -----

class IlacKategori(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to='ilac_kategori_img',null=True,blank=True)

    def __str__(self):
        return self.name

class HassasiyetTuru(models.Model):
    name = models.CharField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.name


class Hastalik(models.Model):
    name = models.CharField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to='form_img', null=True, blank=True)
    def __str__(self):
        return self.name


class Ilac(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    etken_madde = models.CharField(max_length=100, null=True, blank=True)
    kullanim_uyarisi = models.CharField(max_length=300, null=True, blank=True)
    document = models.FileField(upload_to='documents', null=True, blank=True)  # PDF dosyası için alan
    ilac_kategori = models.ForeignKey(IlacKategori, null=True, blank=True, on_delete=models.SET_NULL)
    hassasiyet_turu = models.ForeignKey(HassasiyetTuru, null=True, blank=True, on_delete=models.SET_NULL)
    hastaliklar = models.ManyToManyField(Hastalik, related_name="ilaclar")
    kontsantrasyon_ml = models.DecimalField(max_digits=9, decimal_places=4, null=True,blank=True)
    kontsantrasyon_mg = models.DecimalField(max_digits=9, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return self.name



class YasDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    doz = models.CharField(max_length=200, null=True, blank=True)
    min_yas = models.IntegerField()
    maks_yas = models.IntegerField()

class KiloDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    maksimum_anlik_doz = models.DecimalField(max_digits=8, decimal_places=4, null=True,blank=True)



class ExplanationDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    bilgi = models.TextField(null=True, blank=True)


class HatalikYasDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    hastaliklar = models.ForeignKey(Hastalik, null=True, blank=True, related_name="hastalikyasdoz", on_delete=models.SET_NULL)
    doz = models.CharField(max_length=200, null=True, blank=True)
    min_yas = models.IntegerField()
    maks_yas = models.IntegerField()


class HastalikKiloDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    hastaliklar = models.ForeignKey(Hastalik, null=True, blank=True, related_name="hastalikkilodoz", on_delete=models.SET_NULL)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    maksimum_anlik_doz = models.DecimalField(max_digits=8, decimal_places=4, null=True,blank=True)


class ArtanKiloDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    maksimum_anlik_doz = models.DecimalField(max_digits=8, decimal_places=4, null=True,blank=True)
    threshold_weight = models.IntegerField()
    threshold_weight_min_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_weight_max_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)


class AzalanKiloDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_weight = models.IntegerField()
    threshold_weight_min_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_weight_max_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)


class HastalikArtanKiloDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    hastaliklar = models.ForeignKey(Hastalik, null=True, blank=True, related_name="hastalikartankilodoz", on_delete=models.SET_NULL)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    maksimum_anlik_doz = models.DecimalField(max_digits=8, decimal_places=4, null=True,blank=True)
    threshold_weight = models.IntegerField()
    threshold_weight_min_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_weight_max_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)


class HastalikAzalanKiloDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    hastaliklar = models.ForeignKey(Hastalik, null=True, blank=True, related_name="hastalikazalankilodoz", on_delete=models.SET_NULL)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_weight = models.IntegerField()
    threshold_weight_min_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_weight_max_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)



class HastalikHemYasaHemKiloyaBagliArtanDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    hastaliklar = models.ForeignKey(Hastalik, null=True, blank=True, related_name="hastalikhemyasahemkiloyabagliartandoz", on_delete=models.SET_NULL)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    maksimum_anlik_doz = models.DecimalField(max_digits=8, decimal_places=4, null=True,blank=True)
    threshold_age = models.IntegerField()
    threshold_age_min_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_age_max_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)



class HastalikHemYasaHemKiloyaBagliAzalanDoz(models.Model):
    ilac = models.ForeignKey(Ilac, null=True, blank=True, on_delete=models.CASCADE)
    hastaliklar = models.ForeignKey(Hastalik, null=True, blank=True, related_name="hastalikhemyasahemkiloyabagliazalandoz", on_delete=models.SET_NULL)
    kullanim_sikligi = models.CharField(max_length=150, null=True, blank=True)
    check_uyari = models.TextField(null=True, blank=True)
    tipik_min_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)  # Ondalıklı alan (4 basamak)
    tipik_max_doz = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_age = models.IntegerField()
    threshold_age_min_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    threshold_age_max_dose = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)


# ------ besin takviyeleri ------


class Supplement(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    supplement = models.ForeignKey(Supplement, null=True, blank=True, on_delete=models.SET_NULL)
    img = models.ImageField(upload_to='product_category_img', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    product_category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    explanation = models.TextField(null=True, blank=True)


# ------ hatırlatıcılar -----



class Hatirlatici(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True,blank=True, on_delete=models.CASCADE, related_name='hatirlatici_user')
    form = models.CharField(max_length=50, null=True, blank=True)
    kuvvet = models.CharField(max_length=50, null=True, blank=True)  # 5ml gibi ölçüsü ile birlikte değer olacaktır.
    baslangic_tarihi = models.DateField(blank=True, null=True)
    bitis_tarihi = models.DateField(blank=True, null=True)
    is_removed = models.BooleanField(default=False)
    is_stopped = models.BooleanField(default=False)




class HatirlaticiSaati(models.Model):
    hatirlatici = models.ForeignKey(
        'Hatirlatici',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='hatirlatici_saat'
    )
    saat = models.TimeField(blank=True, null=True)  # Defines the 'saat' field to store time values


    def __str__(self):
        return f"{self.hatirlatici} - {self.saat}"



class Bildirim(models.Model):
    hatirlatici = models.ForeignKey(
        'Hatirlatici',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='hatirlatici_bildirim'
    )
    saat = models.TimeField(blank=True, null=True)
    durum = models.BooleanField(default=False)