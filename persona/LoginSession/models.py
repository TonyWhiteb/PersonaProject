from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,AbstractUser,PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone


#https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser 
#AbstractBaseUser model
# https://github.com/django/django/blob/master/django/contrib/auth/base_user.py
# base_user model


# https://github.com/django/django/blob/master/django/db/models/fields/__init__.py
# django.db.models

class MyUserManager(BaseUserManager):
# https://github.com/django/django/blob/master/django/contrib/auth/base_user.py#L16
# BaseUserManager
    use_in_migrations = True 
# TODO: WHY?  
# FIXME: If set to True the manager will be serialized into migrations and will
#        thus be available in e.g. RunPython operations.

    def _create_user(self,username,password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        username = self.normalize_email(username)    
        # user = self.model(
        #     email=self.normalize_email(email),
        #     # normalize_email is a class method of BaseUserManager
        #     # Normalizes email addresses by lowercasing the domin portion of the eamil address
        #     # https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager
        # )    
        user = self.model(username=username, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, username,  password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
# TODO: setdefault()
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username,  password, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)



        if extra_fields.get('is_staff') is not True:

            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:

            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username,  password, **extra_fields)    

class MyUser(AbstractBaseUser,PermissionsMixin):
    # rebuild my own user model, all steps are the same as AbstractUser's
    # Making email address as username

    # https://github.com/django/django/blob/master/django/contrib/auth/models.py#L288
    # AbstractUser model   

    # https://github.com/django/django/blob/master/django/contrib/auth/base_user.py#L47
    # AbstractBaseUser

    username_validator = UnicodeUsernameValidator()

    username = models.EmailField(
        _('username'),
        max_length = 150,
        unique = True,
        help_text = _('Required valid email address'),
        validators = [username_validator],
        error_messages = {
            'unique': _('A user with that emaill address already exist.'),
        },
    )


    is_staff = models.BooleanField(
        _('staff status'),
        default = False,
        help_text = _(
            'Designates whether the user can log into this admin site.'
        )
    )
    is_active = models.BooleanField(
        _('active'),
        default = True,
        help_text=_(

            'Designates whether this user should be treated as active. '

            'Unselect this instead of deleting accounts.'

        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_admin = models.BooleanField(default = False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'username'

    class Meta:

        verbose_name = _('user')

        verbose_name_plural = _('users')
# AbstractBaseUser methods
# def get_username(self):

#         "Return the identifying username for this User"

#         return getattr(self, self.USERNAME_FIELD)



#     def __str__(self):

#         return self.get_username()



#     def clean(self):

#         setattr(self, self.USERNAME_FIELD, self.normalize_username(self.get_username()))



#     def save(self, *args, **kwargs):

#         super().save(*args, **kwargs)

#         if self._password is not None:

#             password_validation.password_changed(self._password, self)

#             self._password = None



#     def natural_key(self):

#         return (self.get_username(),)



#     @property

#     def is_anonymous(self):

#         """

#         Always return False. This is a way of comparing User objects to

#         anonymous users.

#         """

#         return False



#     @property

#     def is_authenticated(self):

#         """

#         Always return True. This is a way to tell if the user has been

#         authenticated in templates.

#         """

#         return True



#     def set_password(self, raw_password):

#         self.password = make_password(raw_password)

#         self._password = raw_password



#     def check_password(self, raw_password):

#         """

#         Return a boolean of whether the raw_password was correct. Handles

#         hashing formats behind the scenes.

#         """

#         def setter(raw_password):

#             self.set_password(raw_password)

#             # Password hash upgrades shouldn't be considered password changes.

#             self._password = None

#             self.save(update_fields=["password"])

#         return check_password(raw_password, self.password, setter)



#     def set_unusable_password(self):

#         # Set a value that will never be a valid hash

#         self.password = make_password(None)



#     def has_usable_password(self):

#         """

#         Return False if set_unusable_password() has been called for this user.

#         """

#         return is_password_usable(self.password)



#     def get_session_auth_hash(self):

#         """

#         Return an HMAC of the password field.

#         """

#         key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"

#         return salted_hmac(key_salt, self.password).hexdigest()



#     @classmethod

#     def get_email_field_name(cls):

#         try:

#             return cls.EMAIL_FIELD

#         except AttributeError:

#             return 'email'



#     @classmethod

#     def normalize_username(cls, username):

#         return unicodedata.normalize('NFKC', username) if isinstance(username, str) else username

    


