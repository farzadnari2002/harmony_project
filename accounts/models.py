from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone:
            raise ValueError("Users must have an phone number")

        user = self.model(
            phone=phone,
            password=password,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a User with the given phone and password.
        """
        user = self.create_user(
            phone,
            password=password,
            )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه')
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name="آدرس ایمیل"
    )
    username = models.CharField(max_length=32, unique=True, null=True,  blank=True, verbose_name='نام کاربری')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def get_last_otp(self):
        return self.otps.order_by('-created_at').first()
    
    
class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps', verbose_name='کاربر')
    code = models.CharField(max_length=6, verbose_name='کد')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد کد')
    
    
    class Meta():
        verbose_name = 'رمز یکبار مصرف'
        verbose_name_plural = 'رمزهای یکبار مصرف'
        
    def __str__(self):
        return self.code
