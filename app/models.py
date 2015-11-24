from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class server_func_categ(models.Model):
    server_categ_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.server_categ_name

class server_app_categ(models.Model):
    app_categ_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.app_categ_name

class server_list(models.Model):
    server_name = models.CharField(max_length=13)
    server_eip = models.CharField(max_length=15, blank=True)
    server_ip = models.CharField(max_length=15, primary_key=True)
    server_op = models.CharField(max_length=20)
    create_date = models.DateTimeField('Create Date')

    def __unicode__(self):
        #return self.server_name, self.server_ip, self.server_eip, self.server_op
        return self.server_name

    def was_publisthed_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)

class module_list(models.Model):
    module_name = models.CharField(max_length=20)
    module_caption = models.CharField(max_length=255)
    module_extend = models.FileField(max_length=2000)

    def __unicode__(self):
        return self.module_name
