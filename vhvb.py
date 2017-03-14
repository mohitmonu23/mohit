import mysql.connector
con=mysql.connector.connect(user="root",password="",host="localhost",database="mysql")
mycursor=con.cursor()
mycursor.execute("""INSERT INTO `employee` (`FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`) VALUES ('b', 'fefefffe', '22', 'm')""")
con.commit()
