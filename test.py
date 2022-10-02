import mysql.connector
#establising a database connection
database1 = mysql.connector.connect(
    host="127.0.0.1", user="root", passwd="ruFF2004", database="test"
)
#making a cursor, works like a pointer someone said
my_cursor = database1.cursor()
#taking input from user and spliting it lol
id1,name1,age1 = input().split()
#inserting the values that are input by the user into the database
sql = "INSERT INTO test(id,name,age) VALUES (%s, %s, %s)"
val = (id1,name1,age1)
my_cursor.execute(sql,val)
#saving the data in database
database1.commit()