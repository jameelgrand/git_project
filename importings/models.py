from django.db import models

# Create your models here.
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
    file =  models.FileField(upload_to='importings/static/files/')
    def __unicode__(self):
        return self.file.name.split('/')[3]
class activedb(models.Model):
	dbcreds=models.ForeignKey(dbcred)
class activefile(models.Model):
	file_active=models.ForeignKey(File)