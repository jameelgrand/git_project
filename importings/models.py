from django.db import models
import os
from django.core.files.storage import FileSystemStorage
# Create your models here.
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join('', name))
        return name
class dbcred(models.Model):
	cred_name = models.CharField(max_length=80,primary_key=True)
	database = models.CharField(max_length=80)
	user = models.CharField(max_length=80)
	password = models.CharField(max_length=80)
	host = models.CharField(max_length=80)
	port = models.CharField(max_length=80)
	class Meta:
	    db_table = "db_creds"
	def __unicode__(self):
		return self.cred_name
class File(models.Model):
    file =  models.FileField(upload_to='importings/static/files/',storage=OverwriteStorage())
    def __unicode__(self):
        return self.file.name.split('/')[3]
class activedb(models.Model):
	dbcreds=models.ForeignKey(dbcred)
class activefile(models.Model):
	file_active=models.ForeignKey(File)
