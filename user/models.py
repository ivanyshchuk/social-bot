from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from social.utils import first_char


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'user'

    email = models.EmailField(_(u'email'), unique=True)
    first_name = models.CharField(_(u'first name'), max_length=30)
    last_name = models.CharField(_(u'last name'), max_length=30)
    last_activity = models.DateTimeField(_(u'last activity'), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return u'%s %s.' % (self.first_name, self.last_name)

    def get_short_name(self):
        return u'%s %s.' % (first_char(self.last_name),
                            first_char(self.first_name))
