import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql


host_name = "SYSPHARM"
username = "root"
password = "1111"
database_name = "estate"
db = pymysql.connect(host=host_name, port=3306, user=username, passwd=password, db=database_name, charset='utf8')

cursor = db.cursor()
cursor.execute("set names utf8")
db.commit()
PATH_TO_FILE = 'sqlscript'
for line in open(PATH_TO_FILE):
	cursor.execute(line)
db.commit()

servic_key = "WMV3wl%2BU%2BMG%2FOYQK3Wv99q1H79wjvVwIwHEjvrDV3K4gG2h9P1%2BKiB%2FFa1QoYI0yxBpJ3sm1L0OAEam9Rp2sbw%3D%3D"          # 인증키
locate_code = '11380'    # 서울 은평구
contract_date = '201708' # 실거래가 기간

request_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?LAWD_CD=" + locate_code + "&DEAL_YMD=" + contract_date + "&serviceKey=" + servic_key
pparams = {'LAWD_CD': 'value1', 'DEAL_YMD': 'value'}
response = requests.get(request_url)
print(response.content.decode('utf-8'))
soup = BeautifulSoup(response.content.decode('utf-8'), 'xml')
items = soup.find_all('item')

print(items)

