import pymysql


#host_name = localhost
host_name = "SYSPHARM"
username = "root"
password = "1111"
database_name = "dave"
db = pymysql.connect(host=host_name, port=3306, user=username, passwd=password, db=database_name, charset='utf8')

print(db);

cursor = db.cursor()

print(cursor);

sql = "INSERT INTO dave_table(name, age) VALUES ('mkgg', 48);"
cursor.execute(sql)

sql = "SELECT * FROM dave_table"

cursor.execute(sql)
result = cursor.fetchall()
for row in result:
	print(row[0]);
	print(row[1]);
	print(row[2]);
	print(row[3]);

db.commit()

