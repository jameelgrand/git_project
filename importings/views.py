from django.shortcuts import render
import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
from sqlalchemy import create_engine
from datetime import datetime
from django.templatetags.static import static
import os
from importings.forms import dbform,fileform
# Create your views here.
def Home(request):
	form_db = dbform() # A model form
	form_file=fileform()
	return render(request, 'home.html', {'form_db':form_db,'form_file':form_file})
def Accounts(request):
	filename_path=request.GET['filename']
	os_path=os.getcwd()
	url=os_path+"/importings/static/files/"+filename_path
	#import pdb;pdb.set_trace()
	
	error_flag=False
	customer_id=1000
	status="Active"
	audit_name="manual process"
	audit_date=datetime.now()
	filename=url

	db_creds = {"database":"integradb1", "user":"postgres", "password":"postgres", "host":"localhost", "port":"5433"}
	con = pg.connect(**db_creds)
	engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/integradb1')
	df=pd.read_csv(filename,header=0, dtype=object)
	df.to_sql('temp_accounts',engine,index=False)
	cur = con.cursor()
	no_duplicates=True
	success=True
	required_fields=True
	no_errors=False
	try:
		cur.execute("SELECT routing_main,account_nm,account_number,account_type,currency,description_short from temp_accounts")
		cur.execute("SELECT * FROM temp_accounts  where upper(account_nm) in (SELECT account_nm FROM bnk_adm_accounts)")
		k=cur.fetchone()
		if k is not None:
			no_duplicates=False
			print "ERROR:these rows contain duplicate account_nm values"
			print k
			for record in cur:
					print record
			
	except Exception,e:
		print "missed some required fields"
		print e
		required_fields=False
		
	if required_fields and no_duplicates:
		try:
			cur.execute("INSERT INTO bnk_adm_accounts ( business_unit,account_nm,customer_id,bank_nm,bank_status,account_number,account_type,currency,description_short,description_long,legal_name,initiates_wires,initiates_ach,audit_name,audit_dttm ) (SELECT c.company_id,upper(t.account_nm),%s,b.bank_nm,b.status,t.account_number,t.account_type,t.currency,t.description_short,'description_long','',False,False,%s,%s FROM temp_accounts t,gbl_company c,bnk_adm_banks b where c.currency=t.currency and b.routing_main=t.routing_main )", [customer_id,audit_name,audit_date])	
			#cur.execute('DROP TABLE temp_accounts')
		except Exception,e:
			print e
			success=False
		
		if success:
			#validations
			cur.execute("DELETE from  temp_accounts t where t.routing_main in (SELECT routing_main from bnk_adm_banks) and t.currency in (select currency from gbl_company)")
			cur.execute('SELECT COUNT(*) FROM temp_accounts')
			if cur.fetchone()[0] ==0:
				no_errors=True
			else:
				print "failed to load these rows in your CSV file"
				cur.execute("SELECT *  FROM temp_accounts t where t.routing_main not in (SELECT routing_main from bnk_adm_banks) ")	
				
				for record in cur:
					print "routing_main does not exist"
					print record
				cur.execute("SELECT *  FROM temp_accounts t where t.currency not in (select currency from gbl_company) ")	
				
				for record in cur:
					print "currency does not exist"
					print record


			if no_errors or error_flag:
				con.commit()
				if no_errors:
					print "All records imported successfully"
		else:
			pass

	con.close()
	con = pg.connect(**db_creds)
	cur = con.cursor()
	cur.execute('DROP TABLE temp_accounts')
	con.commit()
	con.close()
	return render(request, 'home.html', {'shirts': filename_path})